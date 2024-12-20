def leap_year(year):
    if year%4==0 and year%100!=0 and year%400==0:
        print("Leap year")
    else:
        print("Not Leap year")
year=int(input("Enter year: "))
leap_year(year)