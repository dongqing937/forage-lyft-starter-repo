
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.Willoughby_engine import *
from battery.spindlerbattery import spindlerbattery
from battery.nubbinbattery import nubbinbattery
from tire.carrigan_tire import Carrigan_tire
from tire.octoprime_tires import Octoprime_tire


class CarFactory():

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,sensor):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   spindlerbattery(last_service_date, current_date),
                   Carrigan_tire(sensor))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,sensor):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),
                   spindlerbattery(last_service_date, current_date),
                   Octoprime_tire(sensor))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on,sensor):
        return Car(SternmanEngine(warning_light_is_on), nubbinbattery(last_service_date, current_date),
                   Carrigan_tire(sensor))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,sensor):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),nubbinbattery(last_service_date, current_date),
                   Octoprime_tire(sensor))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,sensor):
        return Car(CapuletEngine(current_mileage, last_service_mileage),nubbinbattery(last_service_date, current_date),
                   Carrigan_tire(sensor))





