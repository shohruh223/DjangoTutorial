from modeltranslation.translator import register, TranslationOptions

from app.models import New


@register(New)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')