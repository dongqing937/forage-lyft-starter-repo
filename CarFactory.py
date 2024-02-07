
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.Willoughby_engine import *
from battery.spindlerbattery import spindlerbattery
from battery.nubbinbattery import nubbinbattery


class CarFactory():

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   spindlerbattery(last_service_date, current_date))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),
                   spindlerbattery(last_service_date, current_date))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on), nubbinbattery(last_service_date, current_date))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),nubbinbattery(last_service_date, current_date))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),nubbinbattery(last_service_date, current_date))





