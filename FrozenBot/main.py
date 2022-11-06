import requests
import math

class GeoApi():
    def __init__(self):
        self.API_KEY = "17d7346c70e83abde4eceb82b84f8c74"#"d81015613923e3e435231f2740d5610b"
        self.LAT = "-24.7859000"#"-35.836948753554054"
        self.LON = "-65.4116600"#"-61.870523905384076"
       
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

if __name__ == "__main__":
    weather = GeoApi()
    if weather.is_hot_in_salta():
        print("Welcome, IS IT HOT! The temparature is : " + str(weather.get_temperature()))
    else:
        print("Welcome! Nice weather, the temparature is : " + str(weather.get_temperature()))
    