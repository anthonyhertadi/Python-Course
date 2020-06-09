tryy = 0
while True:
    print("Enter the required credentials below!")
    username = input("USERNAME : ")
    password = input("PASSWORD : ")
    tryy += 1
    if tryy ==  3:
        print("F*ck off!")
        break
    else:
        if username == "Anthony" and password == "12345":
         print("WELCOME!!!")
    
        else:
         print("Please check if your username and password are correct!")
        continue 

