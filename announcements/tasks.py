from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from celery import shared_task

from desk_messages import settings
from announcements.models import Comment, Announcement, Author


@shared_task
def comment_created(pk, **kwargs):

    comment = Comment.objects.get(pk=pk)
    email = comment.announcement.author.author_name.email
    subject = f'New comment for announcement "{comment.announcement.title}"!'
    text_content = (
        f'Comment: {comment.comment_text}\n'
        f'Go to profile moderate comment -> http://127.0.0.1:8000/own/profile/'
    )
    html_content = (
        f'<b>Comment</b>: <i>{comment.comment_text}</i> <br>'
        '<u>Go to profile moderate comment</u> -> <a href="{% url "author_announcements" %}">Here</a>'
    )
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def comment_accept(pk, **kwargs):

    comment = Comment.objects.get(pk=pk)
    email = comment.author.author_name.email
    subject = 'Your comment was allowed!'
    text_content = (
        f'Comment: {comment.comment_text}\n'
        f'You can check comment here -> http://127.0.0.1:8000/{comment.announcement.id}/'
    )
    html_content = (
        f'<b>Comment</b>: <i>{comment.comment_text}</i> <br>'
        f'<u>You can check comment </u> -> <a href="http://127.0.0.1:8000/{comment.announcement.id}/">Here</a>'
    )
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
