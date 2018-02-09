BaseClass = type("BaseClass",(object,),{})
C1 = type("C1",(BaseClass,),{"x":1})
C2 = type("C2",(BaseClass,),{"x":2})

def MyFactory(myShieet):
    return C1() if myShieet else C2()

m = MyFactory(True)
v = MyFactory(False)

print m.x,v.x
