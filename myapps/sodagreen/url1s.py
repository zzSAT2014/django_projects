from django.conf.urls import url
from views import CategoryIndex


urlpatterns = [url('^$', CategoryIndex.as_view(), name='category'),
               ]
