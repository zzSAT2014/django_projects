from django.conf.urls import url, include
from views import EntryYearArchive, EntryDetail, index, LinkIndex, EntryMonthArchive, LinkDetail
import views


link_patterns = [
    url('^$', LinkIndex.as_view(), name='index'),
    url('^index/$', LinkIndex.as_view()),
    url('^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        LinkDetail.as_view(), name='detail')
    ]

entry_patterns = [
    url('^$', index, name='index'),
    url('^index/$', index),
    url('^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        EntryDetail.as_view(), name='detail'),
    url('^(?P<year>\d{4})/(?P<month>\w{3})/$', EntryMonthArchive.as_view()),
    url('^(?P<year>\d{4})/$', EntryYearArchive.as_view()),
]

category_patterns = [
    url('^$', views.CategoryIndex.as_view(), name='index'),
    url('^index/$', views.CategoryIndex.as_view()),
    url('^(?P<slug>[-\w]+)', views.CategoryDetail.as_view(), name='detail')
]

tag_patterns = [
    url('^$', views.TagIndex.as_view(), name='index'),
    url('^(?P<name>[-\w]+)',  views.tag_detail_view, name='detail'),
]


urlpatterns = [
    url('^entry/', include(entry_patterns, namespace='coltrane_entry')),
    url('^link/', include(link_patterns, namespace='coltrane_link')),
    url('^category/', include(category_patterns, namespace='coltrane_category')),
    url('^tag/', include(tag_patterns, namespace='coltrane_tag')),
]
