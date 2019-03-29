from django.shortcuts import get_object_or_404
from django.db.models import Q, Avg, StdDev, Sum
from django.core.exceptions import *
from django.contrib.postgres.fields import ArrayField
from django.http import HttpResponse, Http404
from postgres_stats.aggregates import Percentile
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Data
from .serializers import DataAirportSerializer, DataCarrierSerializer, DataAirportCarrierSerializer, DataStatisticsSerializer, DataNumbersSerializer, DataMinutesSerializer, DataDescrStatsSerializer
from .exceptions import *

# ...airports/
class AirportsView(generics.ListAPIView):						#1st endpoint

	lookup_field = 'airport_code'
	serializer_class = DataAirportSerializer

	def get_queryset(self):
		return Data.objects.all()

# -...airports/<pk>
class AirportView(generics.ListAPIView):					#1st endpoint
	lookup_field = 'airport_code'
	serializer_class = DataAirportSerializer
	
	def get_queryset(self):
		airport_code = self.kwargs['airport_code']
		airports_to_return = Data.objects.filter(airport_code=airport_code)
		if airports_to_return.count()==0:
			raise AirportNotFound()
		return airports_to_return

#...carriers/  OR ...carriers?aiport=<code>
class CarriersView(generics.ListAPIView):						#2nd and 3rd endpoint

	lookup_field = 'pk'
	serializer_class = DataCarrierSerializer

	def get_queryset(self):

		req=self.request
		airport = req.GET.get('airport')
		carriers_to_return = Data.objects.distinct('carrier_code')
		if carriers_to_return.count()==0:
			raise CarrierNotFound()
		if airport:
			carriers_in_airport_to_return = carriers_to_return.filter(airport_code=airport)
			if carriers_in_airport_to_return.count()==0:
				raise CarrierNotFound()
			return carriers_in_airport_to_return
		else:
			return carriers_to_return

#...carriers/<carrier_code>
class CarrierView(generics.ListAPIView):					#2nd endpoint

	lookup_field = 'carrier_code'
	serializer_class = DataCarrierSerializer

	def get_queryset(self):
		carrier_code = self.kwargs['carrier_code']
		data_to_return = Data.objects.filter(carrier_code=carrier_code)
		if data_to_return.count()==0:
			raise CarrierNotFound()
		return data_to_return

#...statistics/
class ListofStatisticsView(generics.ListCreateAPIView):			#4th endpoint
	lookup_field = 'pk'
	serializer_class = DataStatisticsSerializer
	def get_queryset(self):
		req=self.request
		airport = req.GET.get('airport')
		carrier = req.GET.get('carrier')
		time 	= req.GET.get('time')
		data_to_return = Data.objects.all()
		if data_to_return.count()==0:
			raise StatisticsNotFound()

		if airport and carrier and time:
			q = data_to_return.filter( 
				Q(airport_code	= airport)& 
				Q(carrier_code	= carrier)& 
				Q(time_label	= time))

			if q.count()==0:
				raise StatisticsNotFound()

			return q

		elif airport and carrier:
			q = data_to_return.filter(
				airport_code = airport,
				carrier_code = carrier)

			if q.count()==0:
				raise StatisticsNotFound()

			return q
		else:
			return data_to_return

#...statistics/<pk>
class StatisticsView(generics.RetrieveUpdateDestroyAPIView):	#4th endpoint
	lookup_field = 'pk'
	serializer_class = DataStatisticsSerializer
	def get_queryset(self):
		return Data.objects.all()

#...statistics/numbers?airport=<>&carrier=<>
class NumbersView(generics.ListAPIView):						#5th endpoint

	lookup_field = 'pk'
	serializer_class = DataNumbersSerializer

	def get_queryset(self):

		req=self.request

		airport = req.GET.get('airport')
		carrier = req.GET.get('carrier')
		time = req.GET.get('time')

		if airport and carrier and time:

			return Data.objects.all().filter( 
				Q(airport_code=airport)& 
				Q(carrier_code=carrier)& 
				Q(time_label=time)
				).values(
					'statistics_flights_cancelled',
					'statistics_flights_delayed',
					'statistics_flights_ontime'
				)

		elif airport and carrier:

			return Data.objects.all().filter( Q(airport_code=airport) & Q(carrier_code=carrier)).values(
			'statistics_flights_cancelled',
			'statistics_flights_delayed',
			'statistics_flights_ontime'
			)

		else:
			Data.objects.all()

#...statistics/minutes?airport=<>&carrier=<>
class MinsOfDelayView(generics.ListAPIView):					#6th endpoint

	lookup_field = 'pk'
	serializer_class = DataMinutesSerializer

	def get_queryset(self):

		req=self.request
		
		airport = req.GET.get('airport')
		time = req.GET.get('time')
		reasons= req.GET.getlist('reasons')
		query1 = Data.objects.all()
		query2 = Data.objects.none()

		if airport and time:
			query1=query1.filter(Q(airport_code=airport)&Q(time_label=time))
		elif airport:
			query1=query1.filter(airport_code=airport)
		elif time:
			query1=query1.filter(time_label=time)

		if reasons:
			for r in reasons:
				if r=='carrier' or r=='lateaircraft' or r=='nationalaviationsystem' or r=='security' or r=='total' or r=='weather':
					query2=query2.union(query1.values('statistics_minutesdelayed_' + r))
			return query2
		else:
			return query1

#...statistics/descriptive?airport1=<>&airport2=<>
class DescrStatsView(generics.ListAPIView):						#7th endpoint

	lookup_field = 'pk'
	serializer_class = DataDescrStatsSerializer

	def get_queryset(self):

		req=self.request

		airport1 = req.GET.get('airport1')
		airport2 = req.GET.get('airport2')
		carrier = req.GET.get('carrier')

		if airport1 and airport2 and carrier:

			return Data.objects.all().filter( 
					Q(airport_code=airport1) | 
					Q(airport_code=airport2)
				).filter(
					carrier_code=carrier
				).values(
					'statistics_minutesdelayed_carrier',
					'statistics_minutesdelayed_lateaircraft'
				).annotate(
					mean_carier = Avg('statistics_minutesdelayed_carrier'),
					mean_lateaircraft = Avg('statistics_minutesdelayed_lateaircraft'),
					median_carier=Percentile('statistics_minutesdelayed_carrier', 0.5, output_field=models.FloatField()),
					median_lateaircraft=Percentile('statistics_minutesdelayed_carrier', 0.5, output_field=models.FloatField()),
					std_dev_carrier = StdDev('statistics_minutesdelayed_carrier'),
					std_dev_lateaircraft = StdDev('statistics_minutesdelayed_lateaircraft')
				)

		elif airport1 and airport2:

			return Data.objects.all().filter( 
					Q(airport_code=airport1) | 
					Q(airport_code=airport2)
				).values(
					'statistics_minutesdelayed_carrier',
					'statistics_minutesdelayed_lateaircraft'
				).annotate(
					mean_carier = Avg('statistics_minutesdelayed_carrier'),
					mean_lateaircraft = Avg('statistics_minutesdelayed_lateaircraft'),
					median_carier=Percentile('statistics_minutesdelayed_carrier', 0.5, output_field=models.FloatField()),
					median_lateaircraft=Percentile('statistics_minutesdelayed_carrier', 0.5, output_field=models.FloatField()),
					std_dev_carrier = StdDev('statistics_minutesdelayed_carrier'),
					std_dev_lateaircraft = StdDev('statistics_minutesdelayed_lateaircraft')
				)

