import math
n=int(input())
flag=0
for i in range(1,1+n//2):
	if(n==i*i):
		flag=1
		break;		
if(flag==1):
	print("perfect square")
else
	print("not perfect square")
		