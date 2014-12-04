from django.conf.urls import patterns, url
from wishlist import views

urlpatterns=patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^user/(?P<user_name>\w+)/add_gift$', views.add_gift, name='add_gift'),
	url(r'^user/(?P<user_name>\w+)/update$', views.AddressUpdate.as_view(), name='address_update'),
	url(r'^password$','django.contrib.auth.views.password_change',{'template_name':'wishlist/user_form.html','post_change_redirect':'/email'}),
	url(r'^user/(?P<user_name>\w+)/(?P<slug>[\w\-]+)/edit',views.GiftUpdate.as_view(),name="gift_update"),

	url(r'^user/(?P<user_name>\w+)/(?P<gift_name>[\w\-]+)$', views.gift_detail, name='gift_detail'),

	url(r'^user/(?P<user_name>\w+)/$', views.detail, name='detail'),

	url(r'^login$', views.user_login, name='login'),
	url(r'^logout$', views.user_logout, name='logout'),
	url(r'^email$', views.UserUpdate.as_view(),name='user_update')
	)
	