from models import GeoApi

weather = GeoApi()


if __name__ == "__main__":
    
    if weather.is_hot_in_pehuajo():
        print("Welcome, IS IT HOT! The temparature is : " + str(weather.get_temperature()))
    else:
        print("Welcome! Nice weather, the temparature is : " + str(weather.get_temperature()))
    