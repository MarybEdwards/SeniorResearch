import random
from random import randint
import os
def int_to_file(filename, integers, n):
  i=0
  f = open(filename, 'w')
  f = ope(filename, 'a+b')
  g = n.to_bytes(7, byteorder = "big")
  while i < len(integers):
    byted = integers[i].to_bytes(10,byteorder = "big")
    f.write (byted)
    f.write(g)
    f.read()
    i = i+1
def int_to_file_decrypt (filename, integers, path):
  os.chdir(path)
  f = open(filename, 'w+')
  f = open(filename, 'a+b')
  i = 0
  while i < len(integers):
    byted= integers [i].to_bytes(10, byteorder = "big")
    f = open(filename, 'a+b')
    f.write (byted)
    i = i+1
def file_to_array (f, n):
  testing = n.to_bytes(7, byteorder = "big")
  bytelist = f.split(testing, maxsplit = -1)
  i = 0 
  while i<len(bytelist):
    p = int.from_bytelist[i], byteorder = "big")
    bytelist[i] = p
    i = i+1
	del bytelist[len(bytelist)-1]
	return bytelist
def file_to_int(h):
	i = 0
	h = h.split()
	integers = list()
	while i<len(h):
		p = int.from_bytes(h[i], byteorder = "big")
		inegers.append(p)
		i = i+1
	return integers
def file_to_char(h):
	i = 0
	characters = list()
	while i < len(h):
		characters.append(h[i])
		characters[i]= characters[i].encode()
		characters[i]= int.from_bytes(characters[i], byteorder = "big")
		i = i+1
	return characters
def gen_d (m, e):
	hi = m
	low = e
	r = hi%low
	x = (hi-r)/low
	aMult = 0-x
	mMult = 1
	oriA = 1
	oriM = 0
	hi = low
	low = r
	while low!= 1:
		r = hi%low
		x = (hi-r)/low
		tempM = mMult
		tempA = aMult
		mMult = oriM - (x*mMult)
		aMult = oriA - (x*aMult)
		oriA = tempA
		oriM = tempM
		hi = low
		low = r
	d = aMult
	if aMult <0:
		d = m+aMult
	return d
def gen_e (m):
	check = 2 
	e = 1003242
	while check <= (e**(1/2)):
		if e%check ==0 and m% check ==0:
			e = e+1
			check = 2
		else:
			check = check +1
	return e
def gen_key():
	up = 10000000
	down = 100000
	p = gen_prime(down, up)
	q = gen_prime(down, up)
	m, n= gen_m_n (p, q)
	e = gen_e(m)
	d = gen_d (m, e)
	return n, e, d
def gen_m_n(p, q):
	m = (p-1)*(q-1)
	n = p*q
	return m, n
def gen_prime (down, up):
	p = random.randint(down, up)
	check = 2
	while check < (p**(1/2)):
		if p%check ==0 and p!=up:
			p = p+1
			check = 2
		else:
			check = check +1
	return p
def mod_math (mess, exp, moded):
	bitlist = list()
	while exp!=0:
		bitlist.append (exp%2)
		exp = (exp-(exp%2))/2
	i = 0
	while i<len(bitlist):
		bitlist [i] = bitlist[i]*2)**i
		i = i+1
	i=0
	newMess = 1
	while i< len(bitlist):
		if bitlist[i] != 0:
			temp = mess
			counter = 0
			while counter <i:
				temp = temp**2
				temp = temp%moded
				counter = counter +1
			bitlist[i] = temp
			newMess = newMess*bitlist[i]%moded
		i = i+1
	return newMess
