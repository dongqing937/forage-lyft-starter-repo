import unittest
from datetime import datetime
from battery.nubbinbattery import nubbinbattery
from battery.spindlerbattery import spindlerbattery
from engine.capulet_engine import CapuletEngine
from engine.Willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        testbattery = nubbinbattery(last_service_date, current_date )
        self.assertTrue(testbattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        testbattery = nubbinbattery(last_service_date, current_date)
        self.assertFalse(testbattery.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        testbattery = spindlerbattery(last_service_date, current_date )
        self.assertTrue(testbattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        testbattery = spindlerbattery(last_service_date, current_date)
        self.assertFalse(testbattery.needs_service())

class TestCapulet(unittest.TestCase):

    def test_engine_should_be_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        testengine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(testengine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        testengine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(testengine.needs_service())

class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        testengine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(testengine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        testengine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(testengine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_service(self):
        warning_light_is_on = True
        testengine = SternmanEngine(warning_light_is_on)
        self.assertTrue(testengine.needs_service())


    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        testengine = SternmanEngine(warning_light_is_on)
        self.assertFalse(testengine.needs_service())



if __name__ == '__main__':
    unittest.main()
