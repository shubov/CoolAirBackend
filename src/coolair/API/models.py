from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse as api_reverse
from django.urls import reverse

class Data(models.Model):

    airport_code                                     = models.CharField(max_length=3)
    airport_name                                     = models.CharField(max_length=67)
    carrier_code                                     = models.CharField(max_length=2)
    carrier_name                                     = models.CharField(max_length=28)

    statistics_ofdelays_carrier                      = models.IntegerField()
    statistics_ofdelays_lateaircraft                 = models.IntegerField()
    statistics_ofdelays_nationalaviationsystem       = models.IntegerField()
    statistics_ofdelays_security                     = models.IntegerField()
    statistics_ofdelays_weather                      = models.IntegerField()

    statistics_flights_cancelled                     = models.IntegerField()
    statistics_flights_delayed                       = models.IntegerField()
    statistics_flights_diverted                      = models.IntegerField()
    statistics_flights_ontime                        = models.IntegerField() 
    statistics_flights_total                         = models.IntegerField()

    statistics_minutesdelayed_carrier                = models.IntegerField()
    statistics_minutesdelayed_lateaircraft           = models.IntegerField()
    statistics_minutesdelayed_nationalaviationsystem = models.IntegerField()
    statistics_minutesdelayed_security               = models.IntegerField()
    statistics_minutesdelayed_total                  = models.IntegerField()
    statistics_minutesdelayed_weather                = models.IntegerField()

    time_label                                       = models.CharField(max_length=7)
    time_month                                       = models.IntegerField()
    time_year                                        = models.IntegerField()

    def get_airport_url(self, request):
        return api_reverse("airport_specific", kwargs = {'airport_code': self.airport_code}, request=request)

    def get_carrier_url(self, request):
        return api_reverse("carrier_specific", kwargs = {'carrier_code': self.carrier_code}, request=request)

    def get_statistics_url(self, request):
        return api_reverse("statistics_specific", kwargs = {'pk': self.pk}, request=request)

    class Meta:
        db_table = "data"