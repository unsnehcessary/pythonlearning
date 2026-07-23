age = int(input("How old are you? "))

if age < 13:
    print("Child")

elif age < 18:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior")
