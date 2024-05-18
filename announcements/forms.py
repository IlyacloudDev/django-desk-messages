from django import forms

from allauth.account.forms import SignupForm

from .models import Announcement, Author


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'category', 'announcement_text']


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        Author.objects.create(author_name=user)
        return user
