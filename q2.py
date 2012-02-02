#!/usr/bin/python
a=1
b=2
sum=0
while b<=4000000:
	if b%2 == 0:
		sum = sum + b
	at = a
	a = b
	b = b + at 
print sum
