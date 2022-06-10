#!/usr/bin/env python3

import argparse
import math

parser = argparse.ArgumentParser(description='Recursive compunt interest calculator, rounds up every step of the way.')

parser.add_argument(
	'--initial',
	type=float,
	help='THe initial amount, or loan taken',
)

parser.add_argument(
	'--rate',
	type=float,
	help='The annual interest rate as a decimal (1.2% = 0.012)',
)

parser.add_argument(
	'--months',
	type=int,
	help='Over how many months',
)

args = parser.parse_args()


def getNextMonth(current_month):
	if current_month < 12:
		return current_month + 1
	else:
		return 1


def roundupcent(number):
	number = number * 100
	number = math.ceil(number)
	number = number / 100
	return number


def addInterest(number, rate):
	interest = roundupcent(number * rate)
	number = number + interest
	return number


initial = roundupcent(args.initial)
annual_rate = args.rate

new_amt = addInterest(initial, annual_rate)
monthly_amt = roundupcent(new_amt / 120)

print(monthly_amt)
