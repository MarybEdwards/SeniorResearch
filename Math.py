one = 1
two = 2
zero = 0
half = 0.5
three= 3

def gen_inverse (modulus, integer):
	#generates the modular multiplicative inverse of the integer
	remainder = modulus
	#works off the peicewise equation where:
		#remainder = multiplier(hi)-low
		#inverse(n) = inverse(n-2)-(inverse(n-1)*multiplier(n)) for n<1
		#inverse(1) = 1        inverse(0)=0
	previous = one
	beforePrevious = zero
	hi = modulus
	low = integer 
	while low!= one:
		remainder = hi%low
		multiplier = (hi-remainder)/low
		inverse = beforePrevious-(multiplier*previous)
		beforePrevious= previous
		previous = inverse
		hi = low
		low = remainder
		
	if inverse < zero:
		inverse = modulus+inverse
	return inverse

def add_one(number):
	#increases the number by an increment of one 
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
	publicValue = gen_prime(10000, modulus-one)
	privateValue = gen_inverse (modulus, publicValue)
	return str(sharedValue), str(publicValue), str(privateValue)


def same_number(num1, num2):
	#returns true if the numbers passed in are the same number
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
