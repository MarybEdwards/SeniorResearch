one = 1
two = 2
zero = 0
half = 0.5
three= 3

def gen_inverse (modulus, integer):
	#generates the modular multiplicative inverse of the integer
	remainder = modulus%integer
	#works off the peicewise equation where:
		#inverse = inverse(n-2)-(inverse-1)
	multiplier = (modulus-remainder)/integer
	inverse = zero-coefficient
	oriCoefficient = one
	hi = integer
	low = remainder
	while low!= one:
		remainder = hi%low
		multiplier= (hi-remainder)/low
		tempA = inverse
		inverse = oriCoefficient - (coefficient*inverse)
		oriCoefficient = tempA
		hi = low
		low = remainder
	if inverse < zero:
		inverse = modulus+inverse
	return inverse

def add_one(number):
	number+=one
	return number
	

def gen_key():
	upperBound = 10000000
	lowerBound = 100000
	sameInteger= true
	while sameInteger == true:
		primeNum1 = gen_prime(lowerBound, upperBound)
		primeNum2 = gen_prime(lowerBound, upperBound)
		sameInteger = same_number(primeNum1, primeNum2)
	modulus, sharedValue= gen_totient_product (primeNum1, primeNum2)
	publicValue = gen_prime(10000, modulus-1)
	privateValue = gen_inverse (modulus, publicValue)
	return str(sharedValue), str(publicValue), str(privateValue)


def same_number(num1, num2):
	if num1==num2:
		return true
	else:
		return false


def gen_totient_product(num1, num2):
	totient = (num1-one)*(num2-one)
	product = num1*num2
	return totient, product


def gen_prime (lowerbound, upperbound):
	primeNumber = random.randint(lowerbound, upperbound)
	check = three
 	while check < (primeNumber**(half)):	
 		if primeNumber%check ==zero or primeNumber%two==zero:	
 			add_one(primeNumber)	
 			check = three
		else:	
 			add_one(check)
			add_one(check)
	return primeNumber

def byted_format (number):
	onesAndZeros = list()
	while (number!=zero):
		onesAndZeros.append(number%two)
		number = (number-(number%two))//two
	numBaseTwo = [(onesAndZeros[index]*two)**index for index in range(len(onesAndZeros))]
	return numBaseTwo

def change_message (message, exponent, modulus):
	bitlist = byted_format (exponent)
	newMessage = one
	for looping in range(len(bitlist)):
		if bitlist[looping] != zero:
                    temp = message
                    for counter in range(looping):
                        temp=(temp**two)%modulus
                    newMessage=newMessage*temp%modulus
	return newMessage
