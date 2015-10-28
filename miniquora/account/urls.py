from django.conf.urls import include, url
urlpatterns = [
    url(r'^login/$', 'account.views.login', name='login'),
    url(r'^secret/$', 'account.views.secret',name='secret'),
]
