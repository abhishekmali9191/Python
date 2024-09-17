from abc import ABC , abstractmethod
class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self._status = 'off'

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device Name: {self._name}, Status: {self._status}"

class SmartLight(SmartDevice):
    def __init__(self, name, brightness=0):
        super().__init__(name)
        self._brightness = brightness

    def turn_on(self):
        self._status = 'on'
        return f"{self._name} is now on."

    def turn_off(self):
        self._status = 'off'
        return f"{self._name} is now off."


    def set_brightness(self, level):
        if 0 <= level <= 100:
            self._brightness = level
            return f"Brightness set to {level}%."
        else:
            return "Brightness level must be between 0 and 100."


    def device_info(self):
        return f"Device Name: {self._name}, Status: {self._status}, Brightness: {self._brightness}%"

smart_light = SmartLight("Living Room Light")
print(smart_light.device_info())
print(smart_light.turn_on())
print(smart_light.set_brightness(70))
print(smart_light.device_info())
print(smart_light.turn_off())
print(smart_light.device_info())