#!/usr/bin/python3
import time

myPercent= 0
print('decompressing 0%')

# print a counter overwriting the previous line
while myPercent < 100:
	time.sleep(0.05)
	myPercent += 1
	print(f'\033[Fdecompressing', myPercent, '%')
	
