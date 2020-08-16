def readable_timedelta(days):
    # insert your docstring here
    '''estimates the number of weeks and days from a given amount of days
    INPUT: 
        days - int
    OUTPUT:
        the function returns quotient as number of weeks and remainder as number of days'''

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)