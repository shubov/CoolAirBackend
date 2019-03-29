from rest_framework.exceptions import APIException

class AirportNotFound(APIException):
    status_code = 404
    default_detail = 'Airport Code is wrong. There is no airport mathcing to this code.'

class CarrierNotFound(APIException):
    status_code = 404
    default_detail = 'Carrier Code is wrong. There is no carrier mathcing to this code.'

class AirportNotFound(APIException):
    status_code = 404
    default_detail = 'Airport Code is wrong. There is no airport mathcing to this code.'

class StatisticsNotFound(APIException):
    status_code = 404
    default_detail = 'There is no statistics corresponding to such parameters. Check the query.'









