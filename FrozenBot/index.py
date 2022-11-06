from geoapi import GeoApi
from icecream import IceCream

weather = GeoApi() # Class instance
icecream = IceCream() # Class instance

if __name__ == "__main__":
    
    if weather.is_hot_in_pehuajo():
        print("Welcome, IS IT HOT! The temparature is : " + str(weather.get_temperature()))
    else:
        print("Welcome! Nice weather, the temparature is : " + str(weather.get_temperature()))
    
    print("Ice Cream Flavor")
    print(icecream.get_products())
    while True:
        try:
            print("Please enter a ice cream flavor. Entry correct code, for example")
            sample = icecream.get_products().sample()
            print(f' for {sample["product_name"].unique()} entry code: {sample["code"].unique()}')
            code = int(input("Entry code : "))
            if icecream.is_product_available(code):
                break
            else: print("Oops!  No available.  Try again...")
        except ValueError:
            print("Oops!  That was no valid code.  Try again...")
    
    while True:
        try:
            q = int(input("Quantity :"))
            if icecream.is_stock_available(code, q):
                break
            else: print("Oops!  No stock.  Try again...")
        except ValueError:
            print("Oops!  That was no valid quantity.  Try again...")

    
    #if validate_discount_code("primavera2021"):
    #    print(f'Product : {products[products["code"]==code]["product_name"].unique()}  Quantity : {q}')
    #else: print("Noválido")