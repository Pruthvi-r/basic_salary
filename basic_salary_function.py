def bas_sal(basics):
    ta=0.1*basics
    da=0.12*basics
    gross=basics+da+ta
    print(gross)
basic=int(input("enter the basic:"))
print(bas_sal(basic))
