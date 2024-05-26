from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

import datetime

from celery import shared_task

from desk_messages import settings
from announcements.models import Comment, Announcement, Author, User


@shared_task
def comment_created(pk, **kwargs):

    comment = Comment.objects.get(pk=pk)
    email = comment.announcement.author.author_name.email
    subject = f'New comment for announcement "{comment.announcement.title}"!'
    text_content = (
        f'Comment: {comment.comment_text}\n'
        f'Go to profile moderate comment -> {settings.SITE_URL}/own/profile/'
    )
    html_content = (
        f'<b>Comment</b>: <i>{comment.comment_text}</i> <br>'
        f'<u>Go to profile moderate comment</u> -> <a href="{settings.SITE_URL}own/profile/">'
        f'Here</a>'
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
        f'You can check comment here -> {settings.SITE_URL}{comment.announcement.id}/'
    )
    html_content = (
        f'<b>Comment</b>: <i>{comment.comment_text}</i> <br>'
        f'<u>You can check comment </u> -> <a href="{settings.SITE_URL}{comment.announcement.id}/">'
        f'Here</a>'
    )
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def weekly_notification():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    announcements = set(Announcement.objects.filter(time_in__gte=last_week).order_by('-time_in')[:5])
    users = User.objects.all()
    subject = 'Desk messages is in touch!!'
    html_content = render_to_string(
        'tasks/week_announcements.html',
        {
            'link': settings.SITE_URL,
            'announcements': announcements,
        }
    )
    for user in users:
        msg = EmailMultiAlternatives(
            subject=subject,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
