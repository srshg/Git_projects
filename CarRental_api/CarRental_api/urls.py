from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from CarRental_api import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = [
    url(r'^explorer/$', views.api_root),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='CarRental API', description='RESTful API for CarRental')),
    url(r'^', include('Cars.urls',namespace='cars')),
    url(r'^', include('Rentals.urls',namespace='rentals'))
]


