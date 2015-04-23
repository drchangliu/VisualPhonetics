# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

"""
urlpatterns = patterns('', 
    url(r'^$', 'VowelCatApp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', 'VowelCatApp.views.auth_view'),
    url(r'^logout/$', 'VowelCatApp.views.logout'),
    url(r'^loggedin/$', 'VowelCatApp.views.loggedin'),
    url(r'invalid/$', 'VowelCatApp.views.invalid_login'),
    url(r'^register/', 'VowelCatApp.views.register_user'),
    url(r'^register_success/', 'VowelCatApp.views.register_success'),   
    url(r'^files/', 'VowelCatApp.views.files'),
    url(r'^practice/', 'VowelCatApp.views.practice'),
    url(r'^download/', 'VowelCatApp.views.download'),
    url(r'^listening/', 'VowelCatApp.views.listening'),
    url(r'^training/', 'VowelCatApp.views.training'),
    url(r'^upload/', 'VowelCatApp.views.upload'),
    url(r'^update_user/', 'VowelCatApp.views.update_user'),

)
"""

urlpatterns = i18n_patterns('',
    url(r'^$', 'VowelCatApp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', 'VowelCatApp.views.auth_view', name='auth'),
    url(r'^logout/$', 'VowelCatApp.views.logout', name='logout'),
    url(r'^loggedin/$', 'VowelCatApp.views.loggedin', name='loggedin'),
    url(r'invalid/$', 'VowelCatApp.views.invalid_login', name='invalid'),
    url(r'^register/', 'VowelCatApp.views.register_user', name='register'),
    url(r'^register_success/', 'VowelCatApp.views.register_success', name='register_success'),   
    url(r'^files/', 'VowelCatApp.views.files', name='files'),
    url(r'^practice/', 'VowelCatApp.views.practice', name='practice'),
    url(r'^download/', 'VowelCatApp.views.download', name='download'),
    url(r'^listening/', 'VowelCatApp.views.listening', name='listening'),
    url(r'^training/', 'VowelCatApp.views.training', name='training'),
    url(r'^upload/', 'VowelCatApp.views.upload', name='upload'),
    url(r'^update_user/', 'VowelCatApp.views.update_user', name='update_user'),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,'show_indexes': False}),
)
