from django.conf.urls import url

from . import views
app_name='medicine'
urlpatterns = [

 #   url(r'^$',views.index,name='index'),
# url(r'^$',views.IndexView.as_view(),name='index'),

    # url(r'^register/$', views.register, name='register'),
    #
    # #  url(r'^(?P<album_id>[0-9]+)/$',views.details,name='detail'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'doctors/$', views.doc, name='doctors'),

    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

#url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
]

