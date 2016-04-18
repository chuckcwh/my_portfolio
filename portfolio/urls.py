from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio_app.views.index', name='index'),
    url(r'^blog/', 'portfolio_app.views.blog', name='blog'),
    url(r'^proj/', 'portfolio_app.views.project', name='proj'),


    # Games:
    url(r'^enci_bday', 'enci_bday.views.enci_bday', name='enci_bday'),

    #ajax
    url(r'^email_send/', 'portfolio_app.views.email_send', name='email_send'),

    url(r'^admin/', include(admin.site.urls)),
)
