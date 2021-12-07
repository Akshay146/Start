#number is an Amstrong or not
num=int(input())
sum=0
temp=num
while(temp>0):
	digit=digit%10
	sum=sum+(digit**3)
	digit=digit//10
if num==sum:
	print("amstrong number",num)
else:
	print("not an amstrong number",num)

