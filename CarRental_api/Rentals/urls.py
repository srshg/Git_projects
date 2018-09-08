from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Rentals import views


app_name = 'rentals'

urlpatterns = [
    url(r'^Rentals/(?P<pk>[0-9]+)/highlight/$',views.RentalHighlight.as_view()),
    url(r'^Rentals/$', views.RentalList.as_view(),name='list'),
    url(r'^Rentals/create/$', views.RentalAdd.as_view(), name='create'),
    url(r'^Rentals/(?P<pk>[0-9]+)/$', views.RentalDetail.as_view(),name='details')


]

urlpatterns = format_suffix_patterns(urlpatterns)


