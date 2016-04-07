from django.conf.urls import url , include
from . import views

urlpatterns=[
	url(r'^$',views.show_list,name='show_list'),
	url(r'^addItem/$',views.addItem,name='addItem'),
	url(r'^removeItem/(?P<pk>\d+)/$',views.removeItem,name='removeItem'),
	url(r'^removeItemW/$',views.removeItemW,name='removeItem'),
]