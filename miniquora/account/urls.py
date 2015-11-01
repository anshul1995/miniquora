from django.conf.urls import include, url
urlpatterns = [
    url(r'^logout/$', 'account.views.logout', name = 'logout'),
    url(r'^home/$', 'account.views.home',name='home'),
    url(r'^signup/$', 'account.views.signup',name='signup'),
]
