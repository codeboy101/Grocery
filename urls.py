from django.conf.urls import url , include
from . import views

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^greet/(?P<pk>[0-9]+)/$',views.greet,name='greet'),
]
