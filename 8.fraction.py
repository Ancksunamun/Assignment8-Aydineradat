
print("welcome to fraction program")
a= {"n":1 , "d":1}

b={"n":2 , "d":2}

def summ(a,b):
    return {'n':(a['n']*b['d']+b['n']*a['d']),'d':(a['d']*b['d'])}

def diff(a,b):
    return {'n': (a['n'] * b['d'] - b['n'] * a['d']), 'd': (a['d'] * b['d'])}

def muul(a,b):
    return {'n':(a['n']*b['n']),'d':(a['d']*b['d'])}

def diiv(a,b):
    return {'n':(a['n']*b['d']),'d':(a['d']*b['n'])}

print(summ(a, b))
print(diff(a, b))
print(muul(a, b))
print(diiv(a, b))