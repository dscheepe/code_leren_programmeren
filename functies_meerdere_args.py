"""def begroet(*args):
    for naam in args:
        print(f"Hallo {naam}")

begroet("Inge","Jan","Martien","Mario","Dario")

def vermenigvuldig(*arg):
    res = 1
    for getal in arg:
        res *= getal
    return res

print(vermenigvuldig(5,4,2,10))

"""
getallen = [1,5,8,3,4,1,2,6,8,1]
"""for i in range(getallen.count(1)):
    getallen.remove(1)
print(getallen)"""
getallen = list(set(getallen))
print(getallen)