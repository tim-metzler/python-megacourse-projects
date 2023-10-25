try:
    total_value = int(print("Enter total value"))
    value = int(print("Enter value"))
    percent = value/total_value * 100
    print("That are"+str(percent)+"%")
except TypeError:
    print("Enter a number")
except ZeroDivisionError:
    print("Your total value cannot be zero.")