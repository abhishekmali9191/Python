#Smart Home Device management
from abc import ABC , abstractmethod
class SmartDevice(ABC):
    _name = ""
    _status = ""
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def device_info(self):
        pass
class SmartLight(SmartDevice):
    def __init__(self,name):
        self._name=name
    def turn_on(device:SmartDevice):
        device._status = "ON"
        return "Smart light is now ON..."
    def turn_off(device:SmartDevice):
        device._status = "OFF"
        return "Smart Light is now OFF..."
    def device_info(device:SmartDevice):
        return f"The light {device._name} is {device._status}"

light1 = SmartLight("loyyed")
print(SmartLight.turn_on(light1))
print(SmartLight.device_info(light1))
print(SmartLight.turn_off(light1))
print(SmartLight.device_info(light1))


