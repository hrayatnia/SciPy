import time
def fibo(n):
	a,b=0,1
	temp=0
	for i in range(n):
		temp=a+b
		a=b
		b=temp
	return temp
start = time.clock()
f=open('fibopypy.txt',"w+")
for i in range(1500):
	f.write(str(fibo(i))+"\n")
stop = time.clock()
f.write("time equal ="+str(stop-start))