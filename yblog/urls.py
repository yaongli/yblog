# coding: utf-8
import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^page/(?P<page>\d+)/', 'blog.views.index', name="page"),
    url(r'^blog/(?P<blogid>\d+)/', 'blog.views.showblog', name="showblog"),
    url(r'^bloglist/(?P<page>\d+)/$', 'blog.views.bloglist', name='bloglist'),
    url(r'^login/$', 'blog.views.login', name='login'),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^change_passwd/$', 'blog.views.change_passwd', name='change_passwd'),
    url(r'^addblog/$', 'blog.views.addblog', name='addblog'),
    url(r'^editblog/(?P<blogid>\d+)/$', 'blog.views.editblog', name='editblog'),
    url(r'^saveblog/$', 'blog.views.saveblog', name='saveblog'),
    url(r'^signout/$', 'blog.views.signout', name='signout'),
    url(r'^help/$', 'blog.views.bloghelp', name='bloghelp'),
    url(r'^markdownblog/$', 'blog.views.markdownblog', name='markdownblog'),
    url(r'^markdownblog/(?P<blogid>\d+)/$', 'blog.views.markdownblog', name='markdownblog'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^static/js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),
    #(r'^static/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),
    #(r'^static/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.STATIC_ROOT, 'img')}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns() 