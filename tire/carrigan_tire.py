from tire.tires import Tire

class Carrigan_tire(Tire):

    def __init__(self,sensor):
        self.sensor = sensor

    def needs_service(self):
        if max(self.sensor) >=0.9:
            return True
        return False