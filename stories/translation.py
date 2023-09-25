from modeltranslation.translator import translator, TranslationOptions
from .models import Recipe, Category, Tag


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


translator.register(Recipe, RecipeTranslationOptions)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class TagTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Tag, TagTranslationOptions)
translator.register(Category, CategoryTranslationOptions)