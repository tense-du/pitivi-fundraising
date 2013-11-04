import website.views as v
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
  url(r'^$', v.home),
  url(r'^the-plan', v.plan),
  url(r'^gstreamer', v.gstreamer),
  url(r'^tech-overview', v.tech_overview),
)

urlpatterns += staticfiles_urlpatterns()
