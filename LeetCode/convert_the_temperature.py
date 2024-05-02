from typing import List
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = abs(celsius) + 273.15
        fahrenheit = abs(celsius) * 1.80 + 32.00
        result = [kelvin, fahrenheit]
        return result