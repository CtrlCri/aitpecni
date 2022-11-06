import pandas as pd
class IceCream():
    """
        Ice Cream Flavor Class
    """
    def __init__(self):
        _PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
        "Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})
        self.products =self.__format_products(_PRODUCT_DF)

    def __format_products(self, _PRODUCT_DF: list):
        """
            Format Products

            This function remove out of stock products and 
            assigning a new column for product codes

            Parameters: 
            - _PRODUCT_DF: pandas as list 
    
            Return: 
                - products: a list of product
        """ 
        products = _PRODUCT_DF[_PRODUCT_DF["quantity"]>0] # Only products in stock
        count = len(products.index) # list length
        codes = []
        for i in range(1, count+1):
            codes.append(i)
        products = products.assign(code=codes) # Assignment here

        return products

    def is_product_available(self, code: int):
        """
            Is Product Available

            The function checks if there is a product in the list; 
            returns True if available and False when not

            Parameters: 
                - codes: list 
                - code: int
            Return: 
                - True or False
        """ 
       
        codes = self.products["code"]
        for item in codes:
            if code == item:
                return True
     
        return False
    
    def is_stock_available(self, code: int, q: int):
        quantity_item = int(self.products[self.products["code"]==code]["quantity"])
        if q <= quantity_item:
            return True
        else: 
            return False

    def get_products(self):
        """ Getter """
        return self.products
