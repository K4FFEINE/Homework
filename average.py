#!/usr/bin/env python3

import sys

def main():

#import sy & define function
#pull unlimited numbers from command line using sys.argv
#get the length of the numbers(as in count the number
#of numbers) and put that in a variable called total numbers
#start at counter at 0
#iterate over numbers to get a total
#divide the total by the total numbers and call it average
#print average
	numbers = sys.argv[1:]
	total_numbers = len(numbers)
	total = 0
	for num in numbers:
		total += int(num)
#		return num
	average = total/total_numbers
	print(average)


if __name__ == '__main__':
	main()
