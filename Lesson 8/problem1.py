import time
print("-" * 80)
print("Morbid Predictions Program")


age = input("What is your age? ")
age = int(age)
birthyear = 2018 - age
answer = birthyear + 79
time.sleep(1)
print("...thinking...")
time.sleep(1)
print("...thinking...")
time.sleep(1)
print("...thinking...")
time.sleep(1)

print("You will die in the year " + str(answer))