

from django.conf.urls import url, include
from django.contrib import admin
from show import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.index),
    url(r'^home/', include('myapp.urls')),
]
