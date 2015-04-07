from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

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

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,'show_indexes': False}),
)
