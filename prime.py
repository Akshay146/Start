#program to find a number is prime or not
n=int(input())
flag=False
if n>1:
	for i in range(2,n):
		if(n%i==0):
			flag=True
if flag:
	print("prime number")
else:
	print("is not a prime number")
		