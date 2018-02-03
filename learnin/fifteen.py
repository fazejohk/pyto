def addHam(myfunc):
    def sandwich():
        return myfunc() + " sandwich"
    return sandwich

@addHam
def lul():
    return "this"


print(lul())
