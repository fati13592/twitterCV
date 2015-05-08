from django.conf.urls import patterns, url
from reviews import views

urlpatterns=patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$',views.detail,name='detail'),
	url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
	url(r'^login/$', views.user_login, name='login'),
)
