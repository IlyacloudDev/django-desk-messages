from django import forms
from django.core.exceptions import ValidationError

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'author', 'category', 'announcement_text']
