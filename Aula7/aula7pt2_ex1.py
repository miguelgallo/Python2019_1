import time
# time.time() return the time in seconds since the epoch as a floating point number

def chour(t):
	hour = t / 3600
	print("O número de horas que se passaram desde 01/01/1970 é %f" % hour)

def cminute(t):
	minute = t / 60
	print("O número de minutos que se passaram desde 01/01/1970 é %f" % minute)
	
def cseconds(t):
	seconds = t
	print("O número de segundos que se passaram desde 01/01/1970 é %f" % seconds)
	
def num_day():
	sec = time.time()
	num_day = sec / (60*60*24)
	print("O número de dias que se passaram desde 01/01/1970 é %f" % num_day)

num_day()
chour(time.time())
cminute(time.time())
cseconds(time.time())
