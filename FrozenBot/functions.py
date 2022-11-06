def format_products(_PRODUCT_DF: list):
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

def is_product_available(codes: list, code: int):
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
    for item in codes:
        if code == item:
            return True
     
    return False