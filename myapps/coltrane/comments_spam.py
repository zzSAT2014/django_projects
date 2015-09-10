from akismet import Akismet
from django.conf import settings
from django_comments.models import Comment
from django_comments.signals import comment_will_be_posted
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str
from django.utils import timezone


def moderate_comment(sender, comment, request, **kwargs):
    if not comment.id:
        entry = comment.content_object
        delta = timezone.now() - entry.pub_date
        if delta.days > 30:
            comment.is_public = False
        else:
            akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url="http:/%s/"
                                  % Site.objects.get_current().domain)
        if akismet_api.verify_key():
            akismet_data = {'comment_type': 'comment',
                            'referrer': request.META['HTTP_REFERER'],
                            'user_ip': comment.ip_address,
                            'user_agent': request.META['HTTP_USER_AGENT']}
            print "checking comments successful !"
            if akismet_api.comment_check(smart_str(comment.comment),
                                         data=akismet_data,
                                         build_data=True):
                comment.is_public = False
comment_will_be_posted.connect(moderate_comment, sender=Comment)
