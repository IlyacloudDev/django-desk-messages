from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Announcement, Author, Category, Comment, User


class AnnouncementAdminForm(forms.ModelForm):
    announcement_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Announcement
        fields = '__all__'


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    form = AnnouncementAdminForm
    list_display = ('id', 'title', 'announcement_text', 'author', 'category', 'time_in')
    search_fields = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment_text', 'announcement', 'allowed', 'time_in')
    search_fields = ('author',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = ('username', 'email')
