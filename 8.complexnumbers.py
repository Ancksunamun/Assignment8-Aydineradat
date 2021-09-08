
a={'r':5,'i':3}
b={'r':8,'i':7}


def suum():
    suum={'r':(a['r']+b['r']),'i':(a['i']+b['i'])}
    print(suum)

def diiv():
    diiv={'r':(a['r']-b['r']),'i':(a['i']-b['i'])}
    print(diiv)
def mull():
    mull={'r':((a['r']*b['r'])-(a['i']*b['i'])),'i':((a['i']*b['r'])+(a['r']*b['i']))}
    print(mull)
suum()
diiv()
mull()