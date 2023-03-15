# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def factorial(number):
    if number == 0:
        return 1
    else:
        # recursive call to the function
        return (number * factorial(number - 1))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = int(input("Please enter your number: "))
    if number < 0:
        print(f"Please enter a number greater than or equal to 0")
    else:
        fact = factorial(number)
        print(f"factorial of {number} is {fact}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
