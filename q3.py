
def divide_no():
    try:
        a = float(input("Enter the first number : "))
        b = float(input("Enter the second number : "))
        
        result = a / b
        print(f"The result of {a} / {b} is: {result}")

    except ZeroDivisionError:
        print(" error the number is not divisible by zero.")
    except ValueError:
        print(" error the input is not a numeric value")
    except Exception as e:
        print("unexpected error occurred: {e}")

if __name__ == "__main__":
    divide_no()
