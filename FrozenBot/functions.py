def format_products(_PRODUCT_DF: list):
    """ 
    Remove out of stock products and 
    Assigning a new column for product codes 
    """
    products = _PRODUCT_DF[_PRODUCT_DF["quantity"]>0] # Only products in stock
    count = len(products.index) # list length
    codes = []
    for i in range(1, count+1):
        codes.append(i)
    products = products.assign(code=codes) # Assignment here

    return products

def is_product_available(codes: list, code: int):
    for item in codes:
        if code == item:
            return True
     
    return False