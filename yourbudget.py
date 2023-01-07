import time
import sys
import os
import time
import sys

def load_animation():

	load_str = "starting your console application..."
	ls_len = len(load_str)


	animation = "|/-\\"
	anicount = 0
	
	counttime = 0		
	
	i = 0					

	while (counttime != 100):
		
		time.sleep(0.075)
							
		load_str_list = list(load_str)
		
		x = ord(load_str_list[i])
		
		y = 0							

		if x != 32 and x != 46:			
			if x>90:
				y = x-32
			else:
				y = x + 32
			load_str_list[i]= chr(y)
		
		res =''			
		for j in range(ls_len):
			res = res + load_str_list[j]
			
		sys.stdout.write("\r"+res + animation[anicount])
		sys.stdout.flush()

		load_str = res

		
		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len
		counttime = counttime + 1
	
	if os.name =="nt":
		os.system("cls")
		
	else:
		os.system("clear")

if __name__ == '__main__':
	load_animation()

	s ="Michael"
	sys.stdout.write("Hello "+str(s)+"\n")


print(
"""
██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║██║  ██║██║  ███╗█████╗     ██║   ██║██╔██╗ ██║██║  ███╗
██╔══██╗██║   ██║██║  ██║██║   ██║██╔══╝     ██║   ██║██║╚██╗██║██║   ██║ For Dilling, Created by M
██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████╗   ██║   ██║██║ ╚████║╚██████╔╝ V1.0
╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                         
"""
)

print()

print("finding your device information...")

import platform
 
my_system = platform.uname()
 
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

import sys,time,os

message = print("Before we begin we need to know your name.")
name = input("what is your name? (first and last initial) ")

print("welcome, " + name)


income = int(input("What is your monthly income after taxes? "))
housing = int(input("How much do you spend on housing per month? "))

class Budget:
    def __init__(self, income, housing):
        self.income = income
        self.housing = housing
    
    def needs_budget(self):
        if (housing <= (income * 0.51) and housing >= 0):
            need = (income * 0.6) - housing
        elif (housing > (income * 0.51) and housing < (income * 0.8)):
            need = (income * 0.8) - housing
        else:
            need = (income * .95) - housing
        return need
    
    def save_spend(self):
        if housing <= (income * 0.6):
            save = income * 0.5
            extra = income * 0.5
        elif (housing <= (income * 0.8) and housing >= (income * 0.61)):
            save = income * 0.1
            extra = income * 0.1
        else:
            save = 0
            extra = income - housing - Budget.needs_budget(self)
        return save, extra

class SuperSaver(Budget):    
    def save_spend(self):
        super().save_spend()
        if (housing <= income * .6):
            save = income * 0.3
            extra = income * 0.1
        elif (housing <= (income * 0.8) and housing >= int(income * 0.61)):
            save = income * 0.2
            extra = 0
        else:
            save = income - housing - Budget.needs_budget(self)
            extra = 0
        return save, extra

a_budget = Budget(income, housing)
spending = a_budget.save_spend()

import time 

from tqdm import tqdm

data = [] 


print("your data is now being calculated")

for i in tqdm(range(10)):
	data.append(i)
	time.sleep(.4)


print("On a regular budget...")
print("Your needs budget, after housing costs, is: ")
print(a_budget.needs_budget())
print("Your savings goal per month is: ")
print(spending[0])
print("Your disposable budget is: ")
print(spending[1])

s_budget = SuperSaver(income, housing)
saving = s_budget.save_spend()
print("If you're looking to save more...")
print("Your savings goal per month is: ")
print(saving[0])
print("Your disposable budget is: ")
print(saving[1])

print("thank you!")
