import time
import keyboard
print("HELLO THERE!")
while keyboard.is_pressed('z') == False:
    av = input("AREA//VOLUME? ")
    av.lower()
    if av == "area":
        print("Loading.")
        time.sleep(1)
        print("Loading..")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        print("Loading Complete!")
        print("Pick a Shape!!!")
        shape1 = input("SQUARE//TRIANGLE//CIRCLE? ")
        shape1.lower()
        if shape1 == "square":
            print("Loading.")
            time.sleep(1)
            print("Loading..")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading Complete!")
            base = int(input("ENTER BASE! "))
            length = int(input("ENTER LENGTH! "))
            print("CALCULATING!!!")
            time.sleep(1)
            print(base," x ",length)
            print(base*length)
            extra = input("Again??? y/n ")
            extra.lower()
            if extra == "y":
                continue
            else:
                break
        elif shape1 == "triangle":
            print("Loading.")
            time.sleep(1)
            print("Loading..")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading Complete!")
            base1 = int(input("ENTER BASE! "))
            height = int(input("ENTER HEIGHT! "))
            print("CALCULATING!!!")
            time.sleep(1)
            print(base1," x ",height," x 1/2")
            print(base1*height/2)
            extra = input("Again??? y/n ")
            extra.lower()
            if extra == "y":
                continue
            else:
                break
        elif shape1 == "circle":
            print("Loading.")
            time.sleep(1)
            print("Loading..")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading Complete!")
            rad = int(input("ENTER RADIUS! "))
            print("CALCULATING!!!")
            time.sleep(1)
            print(rad," x ",rad," x 22/7")
            print(rad*rad*22/7)
            extra = input("Again??? y/n ")
            extra.lower()
            if extra == "y":
                continue
            else:
                break
        else:
            print("SYNTAX ERROR!!!")
            continue
    elif av == "volume":
        print("Loading.")
        time.sleep(1)
        print("Loading..")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        print("Loading Complete!")
        print("Pick a Shade!!!")
        shape1 = input("CUBE//TUBE//BALL? ")
        shape1.lower()
        if shape1 == "cube":
            print("Loading.")
            time.sleep(1)
            print("Loading..")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading Complete!")
            base2 = int(input("ENTER BASE! "))
            length2 = int(input("ENTER LENGTH! "))
            height2 = int(input("ENTER HEIGHT! "))
            print("CALCULATING!!!")
            time.sleep(1)
            print(base2," x ",length2," x ",height2)
            print(base2*length2*height2)
            extra = input("Again??? y/n ")
            extra.lower()
            if extra == "y":
                continue
            else:
                break
        elif shape1 == "tube":
            print("Loading.")
            time.sleep(1)
            print("Loading..")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading Complete!")
            rad3 = int(input("ENTER RADIUS! "))
            height3 = int(input("ENTER HEIGHT! "))
            print("CALCULATING!!!")
            time.sleep(1)
            print(rad3," x ",rad3," x ",height3," x 22/7")
            print(rad3*rad3*height3*22/7)
            extra = input("Again??? y/n ")
            extra.lower()
            if extra == "y":
                continue
            else:
                break
        elif shape1 == "ball":
            print("Loading.")
            time.sleep(1)
            print("Loading..")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading Complete!")
            rad4 = int(input("ENTER RADIUS! "))
            print("CALCULATING!!!")
            time.sleep(1)
            print("4/3 x ",rad4," x ",rad4," x ",rad4," x 22/7")
            print(4/3*rad4*rad4*rad4*22/7)
            extra = input("Again??? y/n ")
            extra.lower()
            if extra == "y":
                continue
            else:
                break
        else:
            print("SYNTAX ERROR!!!")
            continue       
    else:
        print("SYNTAX ERROR!!!")
        continue    
