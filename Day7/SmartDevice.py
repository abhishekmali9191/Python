from abc import ABC , abstractmethod
class SmartDevice(ABC):
    def __init__(self, name, status="OFF"):
        self._name = name
        self._status = status

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device Name: {self._name}, Status: {self._status}"

class SmartLight(SmartDevice):
    def turn_on(self):
        self._status = "ON"
        return "Smart light is on"

    def turn_off(self):
        self._status = "OFF"
        return "Smart light is off"

light = SmartLight("Living Room Light")


print(light.device_info())
print(light.turn_on())
print(light.device_info())
print(light.turn_off())
print(light.device_info())