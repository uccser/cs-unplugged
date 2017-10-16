from modeltranslation.translator import translator, TranslationOptions
from topics.models import Topic, UnitPlan, ProgrammingChallenge, ProgrammingChallengeImplementation, Lesson, CurriculumIntegration, GlossaryTerm

class TopicTranslationOptions(TranslationOptions):
    fields = ('name', 'content', 'other_resources')

class UnitPlanTranslationOptions(TranslationOptions):
    fields = ('name', 'content', 'computational_thinking_links')

class ProgrammingChallengeTranslationOptions(TranslationOptions):
    fields = ('name', 'content', 'extra_challenge')

class ProgrammingChallengeImplementationTranslationOptions(TranslationOptions):
    fields = ('expected_result', 'hints', 'solution')

class LessonTranslationOptions(TranslationOptions):
    fields = ('name', 'content')

class CurriculumIntegrationTranslationOptions(TranslationOptions):
    fields = ('name', 'content')

class GlossaryTermTranslationOptions(TranslationOptions):
    fields = ('term', 'definition')



translator.register(Topic, TopicTranslationOptions)
translator.register(UnitPlan, UnitPlanTranslationOptions)
translator.register(ProgrammingChallenge, ProgrammingChallengeTranslationOptions)
translator.register(ProgrammingChallengeImplementation, ProgrammingChallengeImplementationTranslationOptions)
translator.register(Lesson, LessonTranslationOptions)
translator.register(CurriculumIntegration, CurriculumIntegrationTranslationOptions)
translator.register(GlossaryTerm, GlossaryTermTranslationOptions)
