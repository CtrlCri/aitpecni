class DCodes():
    """
        Available Discount Codes Class
    """
    def __init__(self):
        self._AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]
        

    def validate_discount_code(self, discount_code: str):
        """
        Given the list of valid discount codes and a mentioned discount code
        by the client, returns True if the difference between the mentioned code and the codes
        in force is less than three characters, in at least one of the cases

        Example:
        "primavera2021" deberia devolver True, ya que al compararlo:
        vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
        vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o', 'm', 'V',
        'p', 'v')
        vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0', 'x', 'e',
        'd', 'p', 'r')
        vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i', 'v', 'n',
        'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
        """
        count = 3
        i = 0
        l = len(self._AVAILABLE_DISCOUNT_CODES)
        while count >= 3 and i < l: 
            item = self._AVAILABLE_DISCOUNT_CODES[i]
            diff = set(discount_code) ^ set(item) # asymmetric difference
            count = len(diff)
            i += 1
        if count < 3:
            return True
        else: 
            return False  



