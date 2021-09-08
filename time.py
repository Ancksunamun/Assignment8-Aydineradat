
#as seconeds
a=13895

b={'h':12,'m':23,'s':36}

c={'h':6,'m':48,'s':52}

def timesum():
    timesum={}
    timesum['h']=b['h']+c['h']

    if b['m']+c['m']>=60:
        timesum['h']+=1
        timesum['m']=(b['m'] + c['m'])-60
    elif b['m']+c['m']<60:
        timesum['m']=b['m']+c['m']

    if b['s']+c['s']>60:
        timesum['s']=(b['s']+c['s'])-60
        timesum['m']+=1
    elif b['s']+c['s']<=60:
        timesum['s']=b['s']+c['s']
    print(timesum)
def timedif():
    timedif={}
    timedif['h']=b['h']-c['h']
    if b['m']-c['m']<0:
        timedif['m']=-1*(b['m']-c['m'])
        timedif['h']-=1
    elif b['s']-c['s']>=0:
        timedif['m']=b['m']-c['m']
    if b['s']-c['s']<0:
        timedif['s']=-1*(b['s']-c['s'])
        timedif['m']-=1
    print(timedif)

def s2t():
    s2t={}
    s2t['h']=(a//3600)
    s2t['m']=(a%3600)//60
    s2t['s']=(a%3600)%60
    print(s2t)

def t2s():
    t2s=b['h']*3600+b['m']*60+b['s']
    print(t2s)

timesum()
timedif()
s2t()
t2s()