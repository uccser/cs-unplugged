"""Module for custom search view."""
from haystack.generic_views import SearchView
from django.db.models.functions import Concat
from search.forms import CustomSearchForm
from topics.models import (
    CurriculumArea,
    LessonNumber,
)


class CustomSearchView(SearchView):
    """View for custom search."""

    form_class = CustomSearchForm

    def get_context_data(self, *args, **kwargs):
        """Return context dictionary for custom search view.

        Returns:
            Dictionary of context values.
        """
        context = super(CustomSearchView, self).get_context_data(*args, **kwargs)

        # Model filter
        selected_models = self.request.GET.getlist("models")
        models_tuples = context["form"].fields["models"].choices
        models = []
        for (model_value, model_name) in models_tuples:
            model_data = {
                "value": model_value,
                "name": model_name,
            }
            if model_value in selected_models:
                model_data["selected"] = "true"
            models.append(model_data)
        context["models"] = models

        # Curriculum area filter
        selected_curriculum_areas = self.request.GET.getlist("curriculum_areas")
        curriculum_areas = list(CurriculumArea.objects.annotate(
            display_name=Concat("parent__name", "name")
        ).order_by("display_name").values("pk", "colour", "name", "parent__name", "parent__pk"))
        grouped_curriculum_areas = []
        for curriculum_area in curriculum_areas:
            if selected_curriculum_areas:
                if str(curriculum_area["pk"]) in selected_curriculum_areas:
                    curriculum_area["selected"] = "true"
            parent_pk = curriculum_area["parent__pk"]
            if parent_pk:
                grouped_curriculum_areas[-1]["children"].append(curriculum_area)
            else:
                curriculum_area["children"] = []
                grouped_curriculum_areas.append(curriculum_area)
        context["curriculum_areas"] = grouped_curriculum_areas

        # Update result objects
        for result in context["object_list"]:
            if result.model_name == "lesson":
                lesson_ages = []
                for age_group in result.object.age_group.order_by("ages"):
                    number = LessonNumber.objects.get(lesson=result.object, age_group=age_group).number
                    lesson_ages.append(
                        {
                            "lower": age_group.ages.lower,
                            "upper": age_group.ages.upper,
                            "number": number,
                        }
                    )
                result.lesson_ages = lesson_ages
                result.curriculum_areas = CurriculumArea.objects.filter(
                    learning_outcomes__in=result.object.learning_outcomes.all()
                ).distinct()
        return context
