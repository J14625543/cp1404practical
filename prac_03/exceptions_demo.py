while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
    except ValueError:
        print("Numerator and denominator must be valid integers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"The result is: {fraction}")
        break  # 如果一切正常，就跳出循环
print("Finished.")
