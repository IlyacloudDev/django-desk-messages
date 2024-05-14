from django import forms
from django.core.exceptions import ValidationError

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    announcement_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Announcement
        fields = ['title', 'author', 'category']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        announcement_text = cleaned_data.get('announcement_text')

        if title == announcement_text:
            raise ValidationError({
                'Title must not be identical text'
            })
