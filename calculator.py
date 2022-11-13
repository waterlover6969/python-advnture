print ('1. Addition')
print ('2. Subtraction')
print ('3. Multiplication')
print ('4. Division')
print ('5. Edi wag')
while True:
	print ('Choose your operation (1-5): ')
	n = float (input())
	if n>=1 and n<=4:
		print ('Enter two numbers: ')
		num1 = float(input())
		num2 = float (input())
	if n==1:
		print ('Result: ', num1+num2)
	elif n==2:
		print ('Result: ', num1-num2)
	elif n==3:
		print ('Result: ', num1*num2)
	elif n==4:
		print ('Result: ', num1/num2)
	elif n==5:
		print ('FUCK YOU!!!')
		break
	else:
		print('FROM 1 TO 5 IDIOT!!')
	print ('MUY FACIL')