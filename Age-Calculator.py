import time
print("Welcome to my another Programme Age Calculator")
time.sleep(3)
print("In this programme you will be able to calculate your Age..")
time.sleep(3)
print("Loading..")
time.sleep(2)
name = input("Enter your Name :-")
yea = int(input("Enter the Year in which you were born :- "))
future_year = int(input("Enter the year in which you want to know your Age (Eg 2021, 2025 or any else):- "))
calculate = future_year - yea
time.sleep(2)
print("Loading..")
time.sleep(3)
print(name, "would be", calculate, "years old in the year", future_year)
