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
	#previous is used to indicate inverse(n-1)
	beforePrevious = zero
	#beforePrevious is used to indicate inverse(n-2)
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

def add(number, increment):
	#increases the number by some increment 
	number+=increment
	return number
	

def gen_key():
	upperBound = 10000000
	lowerBound = 100000
	sameInteger= true
	while sameInteger == true:
		primeNum1 = gen_prime(lowerBound, upperBound)
		primeNum2 = gen_prime(lowerBound, upperBound)
		sameInteger = same_number(primeNum1, primeNum2)
		#ensures the creation of two very large different prime numbers 
	modulus, sharedValue= gen_totient_product (primeNum1, primeNum2)
	#uses the two prime values to get the totient of the numbers and the product
	publicValue = gen_prime(lowerBound, (modulus-one))
	#the publicly shared value for the key is coprime and smaller than the modulus and a prime value would ensure that 
	privateValue = gen_inverse (modulus, publicValue)
	#the secret value for the private key is the modular multiplicative inverse of publicValue mod(modulus)
	return str(sharedValue), str(publicValue), str(privateValue)


def same_number(num1, num2):
	#returns true if the numbers passed in are the same number
	if num1==num2:
		return true
	else:
		return false


def gen_totient_product(num1, num2):
	#returns the totient (the product of the two numbers with one subtracted from them) and the product of two numbers 
	totient = (num1-one)*(num2-one)
	product = num1*num2
	return totient, product


def gen_prime (lowerbound, upperbound):
	#generates a random prime number
	primeNumber = random.randint(lowerbound, upperbound)
	if primeNumber%two == zero:
		#ensures that it is not even and divisible by two and thus not prime
		primeNumber = add(primeNumber, one)
	#gives a random integer 
	check = three
 	while check < (primeNumber**(half)):	
		#checks through the minimum number of integers before a factor appears if not prime
 		if primeNumber%check ==zero:
			#if the check is evenly divided into the number, it starts again with a new prime number
			primeNumber = add(primeNumber, two)
			#ensures that it only checks odd numbers 
 			check = three
		else:	
			check = add(check, two)
			#finds next number to check that is not even (all even numbers are already divisible by two)
	return primeNumber

def byted_format (number):
	#changes the number into bytes and then into their corresponding powers of two
	onesAndZeros = list()
	while (number!=zero):
		onesAndZeros.append(number%two)
		#creates the list of ones and zeros that is the bytes but backwards when put together
		number = (number-(number%two))//two
	numBaseTwo = [(onesAndZeros[index]*two)**index for index in range(len(onesAndZeros))]
	#raises each number to it's appropriate power of two in the list
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
