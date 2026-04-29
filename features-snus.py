def snus(x):
    print("taste ", x, "snuces")

def comentsnus():
    print("tip for the next question: you'a snusoed now")
    adres = input("enter your homeland: ")
    if adres.count("Snus") or adres.count("snus"):
        print("Well done niga")
    else:
        print("you wasted my time")

print("hi futures snusoyedu")
snus(float(input("your age: ")))
comentsnus()
