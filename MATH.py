def gen_inverse (modulus, integer):
	remainder = modulus%e
	coefficient = (modulus-r)/integer
	aMult = 0-coefficient
	oriA = 1
	hi = integer
	low = remainder
	while low!= 1:
		remainder = hi%low
		coefficient= (hi-remainder)/low
		tempA = aMult
		aMult = oriA - (coefficient*aMult)
		oriA = tempA
		hi = low
		low = remainder
	inverse = aMult
	if aMult <0:
		inverse = modulus+aMult
	return inverse

def add_one(number):
	number+=1
	return number
	

def gen_key():
	upperBound = 10000000
	lowerBound = 100000
	sameInteger= true
	while sameInteger == true:
		primeNum1 = gen_prime(lowerBound, upperBound)
		primeNum2 = gen_prime(lowerBound, upperBound)
		if primeNum1!=primeNum2:
			sameInteger = false
	modulus, sharedValue= gen_m_n (primeNum1, primeNum2)
	publicValue = gen_prime(10000, modulus)
	privateValue = gen_inverse (modulus, publicValue)
	return sharedValue, publicValue, privateValue


def gen_m_n(num1, num2):
	m = (num1-1)*(num2-1)
	n = num1*num2
	return m, n


def gen_prime (lowerbound, upperbound):
	primeNumber = random.randint(lowerbound, upperbound)
	check = 2
	while primeNumber<upperbound:
 		while check < (primeNumber**(0.5)):	
 			if primeNumber%check ==0 and primeNumber!=upperbound:	
 				add_one(primeNumber)	
 				check = 2	
 			else:	
 				add_one(check)
	return primeNumber

def byted_format (number):
	onesAndZeros = list()
	while (number!=0):
		onesAndZeros.append(number%2)
		number = (number-(number%2))//2
	numBaseTwo = [(onesAndZeros[index]*2)**index for index in range(len(onesAndZeros))]
	return numBaseTwo

def change_message (message, exponent, modulus):
	bitlist = byted_format (exponent)
	newMessage = 1
	for looping in range(len(bitlist)):
		if bitlist[looping] != 0:
                    temp = message
                    for counter in range(looping):
                        temp=(temp**2)%modulus
                    newMessage=newMessage*temp%modulus
	return newMessage
