sunday_number = 0
year = 1901
days_until_next_sunday = 5
days_in_year = 365

firsts_in_year = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
firsts_in_leap_year = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

while year < 2001:
    day = 1
    print(year)

    if (year % 4) == 0:
        days_in_year = 366
    else:
        days_in_year = 365

    while day <= days_in_year:
        if(days_until_next_sunday == 0):

            if(days_in_year == 365):
                if(day in firsts_in_year):
                    sunday_number += 1
                    print(sunday_number)
            elif (day in firsts_in_leap_year):
                sunday_number += 1
                print(sunday_number)
            days_until_next_sunday = 6
        else:
            days_until_next_sunday -= 1
        day += 1
    year += 1

print(sunday_number)
print(days_until_next_sunday)
