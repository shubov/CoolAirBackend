from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from API.views import AirportView, AirportsView, CarrierView, CarriersView, ListofStatisticsView, StatisticsView, NumbersView, MinsOfDelayView, DescrStatsView


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/$', RedirectView.as_view(url='https://documenter.getpostman.com/view/6768072/S11Lscpb'),   name='api_docs'),

    url(r'^api/(?P<version>(v1))/airports/$',                           AirportsView.as_view(),          name='airport_list'),
    url(r'^api/(?P<version>(v1))/airport/(?P<airport_code>\w+)/$',     AirportView.as_view(),           name='airport_specific'),

    url(r'^api/(?P<version>(v1))/carriers/$',                          CarriersView.as_view(),          name='carriers_list'),
    url(r'^api/(?P<version>(v1))/carrier/(?P<carrier_code>\w+)/$',     CarrierView.as_view(),           name='carrier_specific'),

    url(r'^api/(?P<version>(v1))/statistics/$',                                               
        ListofStatisticsView.as_view(),  
        name='statistics_list'),

    url(r'^api/(?P<version>(v1))/statistics/(?P<pk>\d+)/$',                                   
        StatisticsView.as_view(),        
        name='statistics_specific'), 

    url(r'^api/(?P<version>(v1))/statistics/numbers/$',                                       
        NumbersView.as_view(),           
        name='numbers_list'),

    url(r'^api/(?P<version>(v1))/statistics/minutes/$',                                       
        MinsOfDelayView.as_view(),       
        name='minutes_list'),

    url(r'^api/(?P<version>(v1))/statistics/descriptive/$',                                   
        DescrStatsView.as_view(),        
        name='delays_list')

    ]