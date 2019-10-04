from django.conf.urls import url, include

from myapp.views import lover,account,ajax,text

urlpatterns = [
     url(r'^$', lover.show),

     url(r'^login/$',account.login,name="aa"),
     url(r'^login/index/$', lover.index),

     url(r'^login/index/logout/$', account.logout),

     url(r'^login/index/other/$', lover.other),

     url(r'^ajax_show/$', ajax.ajax_show),

     url(r'^text_show/$', text.text_show),

]
