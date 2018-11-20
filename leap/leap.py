def is_leap_year(year):
    """Find the Modulus of year"""
    mod_4 = year % 4
    mod_100 = year % 100
    mod_400 = year % 400
    
    """
    Test if the year is a leap year
    Leap year conditions 
        on every year that is evenly divisible by 4
         except every year that is evenly divisible by 100
          unless the year is also evenly divisible by 400
    """
    if mod_400 == 0:
        return True
    elif mod_100 == 0:
        return False
    elif mod_4 == 0:
        return True
    else:
        return False