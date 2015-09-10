from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField
from django.conf import settings
from markdown import markdown
import pydelicious
from django.utils.encoding import smart_str
import comments_spam


class Category(models.Model):

    title = models.CharField(max_length=250, help_text='MaxChar Allowed: 250')
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('coltrane_category:detail', (), {'slug': self.slug})

# entry_model


class LiveEntryManager(models.manager.Manager):

    def all(self):
        # print "getting live entries"
        # print super(LiveEntryManager, self).all().filter(status=Entry.LIVESTATUS)
        return super(LiveEntryManager, self).all().filter(status=Entry.LIVESTATUS)


class Entry(models.Model):

    LIVESTATUS = 1
    DRAFTSTATUS = 2
    HIDDENSTATUS = 3

    title = models.CharField(max_length=250, help_text='MaxChar Allowed: 250')
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    STATUS_CHOICE = [(LIVESTATUS, 'live status'),
                     (DRAFTSTATUS, 'draft status'),
                     (HIDDENSTATUS, 'hidden status'),
                     ]
    status = models.IntegerField(choices=STATUS_CHOICE, default=DRAFTSTATUS)
    live = LiveEntryManager()
    objects = models.manager.Manager()
    tags = TagField()
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        # return '/weblog/%s/%s/' % (self.pub_date.strftime('%Y/%b/%d').lower(), self.slug)
        return ('coltrane_entry:detail', (), {'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime('%d'),
                                              'slug': self.slug}
                )


# link_model


class Link(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    url = models.URLField(unique=True)

    pub_date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')

    tags = TagField()
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to Delicious', default=True)

    via_name = models.CharField('Via', max_length=250, blank=True,
                                help_text='The name of the person whose site you spotted the link on.')
    via_url = models.URLField('Via URL', blank=True,
                              help_text='The URL of the site where you spotted the site')

    class Meta:
        ordering = ['-pub_date']

    def save(self):
        if self.description:
            self.description_html = markdown(self.description)
        if not self.id and self.post_elsewhere:
            try:
                pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD,
                                smart_str(self.url), smart_str(self.title), tags=smart_str(self.tags))
            except pydelicious.DeliciousError:
                pass
        super(Link, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('coltrane_link:detail', (), {'year': self.pub_date.strftime("%Y"),
                                             'month': self.pub_date.strftime("%b").lower(),
                                             'day': self.pub_date.strftime('%d'),
                                             'slug': self.slug}
                )


