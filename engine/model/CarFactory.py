from abc import ABC, abstractmethod

from engine.model.engine import Engine
from engine.model import car
from engine.model.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from engine.model.spindlerbattery import spindlerbattery


class CarFactory():
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    @abstractmethod
    def create_car(self):
        pass


class calliopeFactory(CarFactory):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_car(self):
        return car(CapuletEngine(self.last_service_date, self.current_mileage, self.last_service_mileage),spindlerbattery(self.last_service_date,self.current_date))


class glissadeFactory(CarFactory):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def creat_car(self):
        return car(WilloughbyEngine(self.last_service_date, self.current_mileage, self.last_service_mileage),spindlerbattery(self.last_service_date,self.current_date))


class palindromeFactory(CarFactory):
    def __init__(self,current_date, last_service_date, warning_light_on):
        super().__init__(current_date, last_service_date)
        self.warning_light_on = warning_light_on

    def create_car(self):
        return car(SternmanEngine(self.last_service_date, self.warning_light_is_on),nubbinbattery(self.last_service_date,self.current_date))


class rorschachFactory(CarFactory):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def creat_car(self):
        return car(WilloughbyEngine(self.last_service_date, self.current_mileage, self.last_service_mileage),nubbinbattery(self.last_service_date,self.current_date))


class thovex(CarFactory):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage


    def create_car(self):
        return car(CapuletEngine(self.last_service_date, self.current_mileage, self.last_service_mileage),nubbinbattery(self.last_service_date,self.current_date))




