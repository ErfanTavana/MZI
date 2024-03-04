from django.contrib import admin

from .models import CategoryArticle


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(CategoryArticle, CategoryAdmin)

from .models import TagArticle


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(TagArticle, TagAdmin)

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'display_categories', 'display_tags']
    search_fields = ['title', 'description', 'categories__name', 'tags__name']
    filter_horizontal = ['categories', 'tags']

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    def display_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])

    display_categories.short_description = 'دسته بندی‌ها'
    display_tags.short_description = 'برچسب‌ها'


admin.site.register(Article, ArticleAdmin)
