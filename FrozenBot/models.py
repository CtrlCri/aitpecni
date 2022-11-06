import requests
import math

class GeoApi():
    def __init__(self):
        self.API_KEY = "17d7346c70e83abde4eceb82b84f8c74"#"d81015613923e3e435231f2740d5610b"
        self.LAT = "-35.836948753554054"#"-24.7859000" Pehuajo / Salta respectivamente
        self.LON = "-61.870523905384076"#"-65.4116600" Pehuajo / Salta respectivamente
       
        parameters = {"lat": self.LAT, "lon": self.LON, "appid": self.API_KEY}
        self.temperature = None
        try:
            results = requests.get("https://api.openweathermap.org/data/2.5/weather", parameters)    
            temp_kelvin = results.json()["main"]["temp"]
       
            self.temperature = math.trunc((temp_kelvin - 273.15)) # convierte de kelvin a celcius
        except Exception as e:
                print("One exception:", type(e).__name__, e.args)    

    def is_hot_in_salta(self):
        try:
            t =  self.temperature
            if t > 28:
                return True
            else: 
                return False
        except Exception as e:
            print("One exception:", type(e).__name__, e.args)
            return False
            
    def get_temperature(self):
        return self.temperature
