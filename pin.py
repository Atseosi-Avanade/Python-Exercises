#! /bin/python

#! /bin/python
#Author: Atseosi Idogho
#Description: Similation of a pin machine

import sys

master_pin = "29320"
pin = None
attempts = 3

while attempts > 0:
    pin = input("Please enter your pin number: ")
    if pin == master_pin:
        print("Access Granted")
        break
    else:
        attempts = attempts - 1
        print(f"Entered Pin is invalid {attempts} Attempts remaining")
if attempts == 0:
    print("Your access to this account has been blocked. Please message account administator")
else:
    print("Done")
sys.exit(0)
