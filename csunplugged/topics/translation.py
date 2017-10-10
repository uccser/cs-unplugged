from modeltranslation.translator import translator, TranslationOptions
from topics.models import Topic

class TopicTranslationOptions(TranslationOptions):
    fields = ('name', 'content', 'other_resources')

translator.register(Topic, TopicTranslationOptions)
