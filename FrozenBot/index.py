from models import GeoApi
from functions import format_products, is_product_available

import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})

products = format_products(_PRODUCT_DF)

weather = GeoApi() # Class instance

if __name__ == "__main__":
    
    if weather.is_hot_in_pehuajo():
        print("Welcome, IS IT HOT! The temparature is : " + str(weather.get_temperature()))
    else:
        print("Welcome! Nice weather, the temparature is : " + str(weather.get_temperature()))
    
    print("Ice Cream Flavor")
    print(products)
    while True:
        try:
            print("Please enter a ice cream flavor. Entry correct code, for example")
            sample = products.sample()
            print(f' for {sample["product_name"].unique()} entry code: {sample["code"].unique()}')
            code = int(input("Entry code : "))
            if is_product_available(products["code"], code):
                break
            else: print("Oops!  No available.  Try again...")
        except ValueError:
            print("Oops!  That was no valid code.  Try again...")