from rest_framework import serializers 
from .models import Data
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

## Custom serializer for adding extra fields
class CustomSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

## 1st endpoint
class DataAirportSerializer(serializers.ModelSerializer):
	
	airport_url = serializers.SerializerMethodField(read_only=True)
	airports_list_url = serializers.SerializerMethodField(read_only=True)
	statistics_list_url = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Data
		fields = (
			'pk',
			'airport_url',
			'airports_list_url',
			'statistics_list_url',
			'carrier_code',
			'carrier_name',
			'airport_code',
			'airport_name',
			'time_label')

	def get_airport_url(self, obj):
		return obj.get_airport_url(self.context.get("request"))

	def get_airports_list_url(self, obj):
		return api_reverse('airport_list', request=self.context.get("request"))

	def get_statistics_list_url(self, obj):
		return api_reverse('statistics_list', request=self.context.get("request"))

## 2nd endpoint
class DataCarrierSerializer(serializers.ModelSerializer):

	carrier_url = serializers.SerializerMethodField(read_only=True)
	carriers_list_url = serializers.SerializerMethodField(read_only=True)
	statistics_list_url = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Data
		fields = (
			'pk',
			'carrier_url',
			'carriers_list_url',
			'statistics_list_url',
			'carrier_code',
			'carrier_name',
			'airport_code',
			'airport_name',
			'time_label')

	def get_carrier_url(self, obj):
		return obj.get_carrier_url(self.context.get("request"))

	def get_carriers_list_url(self, obj):
		return api_reverse('carriers_list', request=self.context.get("request"))

	def get_statistics_list_url(self, obj):
		return api_reverse('statistics_list', request=self.context.get("request"))

## 3d endpoint
class DataAirportCarrierSerializer(serializers.ModelSerializer):
	carrier_url = serializers.SerializerMethodField(read_only=True)
	carriers_list_url = serializers.SerializerMethodField(read_only=True)
	statistics_list_url = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Data
		fields = (
			'pk',
			'carrier_url',
			'carriers_list_url',
			'statistics_list_url',
			'carrier_code',
			'carrier_name',
			'airport_code',
			'airport_name', 
			'time_label')

	def get_carrier_url(self, obj):
		return obj.get_carrier_url(self.context.get("request"))

	def get_carriers_list_url(self, obj):
		return api_reverse('carriers_list', request=self.context.get("request"))

	def get_statistics_list_url(self, obj):
		return api_reverse('statistics_list', request=self.context.get("request"))

## 4th endpoint
class DataStatisticsSerializer(CustomSerializer):

	statistics_url = serializers.SerializerMethodField(read_only=True)
	statistics_list_url = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Data
		fields = ('__all__')
		extra_fields = [
			'statistics_url',
			'statistics_list_url']

	def get_statistics_url(self, obj):
		return obj.get_statistics_url(self.context.get("request"))

	def get_statistics_list_url(self, obj):
		return api_reverse('statistics_list', request=self.context.get("request"))

## 5th endpoint
class DataNumbersSerializer(serializers.ModelSerializer):

	numbers_url = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Data
		fields = (
			'pk',
			'numbers_url',
			'statistics_flights_cancelled',
			'statistics_flights_delayed',
			'statistics_flights_ontime')

	def get_numbers_url(self, obj):
		return api_reverse('numbers_list', request=self.context.get("request"))

## 6th endpoint
class DataMinutesSerializer(serializers.ModelSerializer):

	minutes_url = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Data
		fields = (
			'pk',
			'minutes_url',
			'statistics_minutesdelayed_carrier',
			'statistics_minutesdelayed_lateaircraft',
			'statistics_minutesdelayed_nationalaviationsystem',
			'statistics_minutesdelayed_security',
			'statistics_minutesdelayed_total',
			'statistics_minutesdelayed_weather')

	def get_minutes_url(self, obj):
		return api_reverse('minutes_list', request=self.context.get("request"))

## 7th endpoint
class DataDescrStatsSerializer(serializers.ModelSerializer):

	delays_url = serializers.SerializerMethodField(read_only=True)
	mean_carier = serializers.FloatField()
	mean_lateaircraft = serializers.FloatField()
	median_carier = serializers.FloatField()
	median_lateaircraft = serializers.FloatField()
	std_dev_carrier = serializers.FloatField()
	std_dev_lateaircraft = serializers.FloatField()

	class Meta:
		model = Data
		fields = (
			'pk',
			'delays_url',
			'mean_carier',
			'mean_lateaircraft',
			'median_carier',
			'median_lateaircraft',
			'std_dev_carrier',
			'std_dev_lateaircraft',
			'statistics_minutesdelayed_carrier',
			'statistics_minutesdelayed_lateaircraft')

	def get_delays_url(self, obj):
		return reverse('delays_list', request=self.context.get("request"))