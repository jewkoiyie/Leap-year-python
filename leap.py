def leapyear(year):
    leap = False
    #Logical Body
    if year % 4 == 0:
        leap = True
        if year % 100 ==0 and year % 400!=0:
                leap = False
        elif year % 400:
                leap = True
    return leap
#input and output Respectively
year = int(input())
print(leapyear(year))
