numFrom = int(input('From :  '))
numTo = int(input('To :  '))

for num in range(numFrom,numTo+1):
	with open(str(num)+'.py','w') as file:
		pass