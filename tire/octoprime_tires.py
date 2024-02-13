from tire.tires import Tire


class Octoprime_tire(Tire):

    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        if sum(self.sensor) >= 3:
            return True
        return False
