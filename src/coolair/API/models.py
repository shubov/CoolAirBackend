from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse as api_reverse
from django.urls import reverse

class Data(models.Model):

    airport_code                                     = models.CharField(max_length=3, blank=True, null=True)
    airport_name                                     = models.CharField(max_length=67, blank=True, null=True)
    carrier_code                                     = models.CharField(max_length=2, blank=True, null=True)
    carrier_name                                     = models.CharField(max_length=28, blank=True, null=True)

    statistics_ofdelays_carrier                      = models.IntegerField(blank=True, null=True)
    statistics_ofdelays_lateaircraft                 = models.IntegerField(blank=True, null=True)
    statistics_ofdelays_nationalaviationsystem       = models.IntegerField(blank=True, null=True)
    statistics_ofdelays_security                     = models.IntegerField(blank=True, null=True)
    statistics_ofdelays_weather                      = models.IntegerField(blank=True, null=True)

    statistics_flights_cancelled                     = models.IntegerField(blank=True, null=True)
    statistics_flights_delayed                       = models.IntegerField(blank=True, null=True)
    statistics_flights_diverted                      = models.IntegerField(blank=True, null=True)
    statistics_flights_ontime                        = models.IntegerField(blank=True, null=True)
    statistics_flights_total                         = models.IntegerField(blank=True, null=True)

    statistics_minutesdelayed_carrier                = models.IntegerField(blank=True, null=True)
    statistics_minutesdelayed_lateaircraft           = models.IntegerField(blank=True, null=True)
    statistics_minutesdelayed_nationalaviationsystem = models.IntegerField(blank=True, null=True)
    statistics_minutesdelayed_security               = models.IntegerField(blank=True, null=True)
    statistics_minutesdelayed_total                  = models.IntegerField(blank=True, null=True)
    statistics_minutesdelayed_weather                = models.IntegerField(blank=True, null=True)

    time_label                                       = models.CharField(max_length=7, blank=True, null=True)
    time_month                                       = models.IntegerField(blank=True, null=True)
    time_year                                        = models.IntegerField(blank=True, null=True)

    def get_airport_url(self, request):
        return api_reverse("airport_specific", kwargs = {'airport_code': self.airport_code}, request=request)

    def get_carrier_url(self, request):
        return api_reverse("carrier_specific", kwargs = {'carrier_code': self.carrier_code}, request=request)

    class Meta:
        db_table = "data"