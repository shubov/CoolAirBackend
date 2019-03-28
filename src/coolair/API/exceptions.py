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

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'










