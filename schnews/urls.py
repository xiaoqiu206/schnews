from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schnews.views.home', name='home'),
    # url(r'^schnews/', include('schnews.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'schapp.views.index'),
    url(r'^index/', 'schapp.views.index'),
    url(r'^newsList/', 'schapp.views.newsList'),
    url(r'^register/', 'schapp.views.register'),
    url(r'^login/', 'schapp.views.login'),
    url(r'^registerSuccess', 'schapp.views.registerSuccess'),
    url(r'^ajax_list', 'schapp.views.ajax_list')
)
