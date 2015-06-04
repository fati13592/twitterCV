from django.conf.urls import patterns, url
from reviews import views

urlpatterns=patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$',views.detail,name='detail'),
	#url(r'^user/register/$', views.register, name='register'), #esto los usaba antes
	#url(r'^user/login/$', views.user_login, name='login'),		#ahora uso Django-Registration-Redux
	#url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^photos/$', views.find_photos, name='photos'),
)
