from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, about, contests, connect, contact, friend, signup, campaigns, campone, camptwo, campthree, ts, reffered, feedback, error

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CS399Agency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^about', about),
    url(r'^contests', contests),
    url(r'^connect', connect),
    url(r'^contact', contact),
    url(r'^friend', friend),
    url(r'^signup', signup),
    url(r'^campaigns', campaigns),
    url(r'^campone', campone),
    url(r'^camptwo', camptwo),
    url(r'^campthree', campthree),
    url(r'^ts', ts),
    url(r'^reffered', reffered),
    url(r'^feedback', feedback),
    url(r'^404', error)
)
