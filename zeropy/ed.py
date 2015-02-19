import time
def ed(n):
	counter=0
	for i in range(1,n+1):
		if n%i==0:
			counter+=1
	if counter==8:
		return 1

x=10**12
answer=0
t0=time.clock()
for i in range(x):
	if ed(i):
		answer+=1
	print(i)
t1=time.clock()
fil=open("log.txt","w+")
fil.writeline(answer)
tf=t1-t0
fil.write(tf)