#week 5 exercise 2
key = True
while key == True:
    adress = input("please enter your e-mail adress: ")
    if "@" and "." in adress:
            print("welcome to the system!")
            key = False
    else:
        print("please enter a valid adress")
        key = True


