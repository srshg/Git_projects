from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Cars import views


app_name = 'cars'

urlpatterns = [
    url(r'^Cars/(?P<pk>[0-9]+)/highlight/$',views.CarHighlight.as_view()),
    url(r'^Cars/$', views.CarList.as_view(),name='list'),
    url(r'^Cars/create/$', views.CarAdd.as_view(), name='create'),
    #url(r'^Cars/delete/(?P<pk>[0-9]+)/$',views.CarDelete.as_view(), name='deletecar'),
    url(r'^Cars/(?P<pk>[0-9]+)/$', views.CarDetail.as_view(),name='details')


]

urlpatterns = format_suffix_patterns(urlpatterns)