
def info(name, age, filename='info.txt'):
    with open(filename, 'w') as file:
        file.write(f"Name: {name}")
        file.write(f"Age: {age}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    info(name,age)
    print(f"Your name is{name} and age is{age}")