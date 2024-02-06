from engine.model import engine
from battery import battery


class car():
    def __init__(self,engine,battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.need_service() or self.battery.needs_service()