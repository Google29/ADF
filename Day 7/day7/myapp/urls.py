from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.level,name='Ram'),
    url(r'^result',views.create,name='finished')
]