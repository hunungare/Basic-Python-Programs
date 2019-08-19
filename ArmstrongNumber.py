#To find Armstrong numbers in the range 1 to 1000
for i in range(1001):
	num=i
	#To count the digits in number
	n=len(str(num))  
	result=0
	while(i!=0):
		#To access last digit of the number
		digit=i%10
		#To find addition of nth power of n digits in number 
		result=result+digit**n
		#To find next previous digit in number
		i=i//10
	if(num==result):
		print(num)
