import unittest
from count_unique_names import get_max_typos,change_max_typos, countUniqueNames
from names_testing import MyTestCase

def menu():
    welcome_message()
    user_input = -1
    while (user_input != 0):
        print_menu()
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            user_input = -1
        if user_input == 1:
            edit_max_typos()
        elif user_input == 2:
            print_max_typos()
        elif user_input == 3:
            run_all_tests()
        elif user_input == 4:
            run_manual_test()
        elif user_input == 0:
            print("Exiting...")
        else:
            print("Invalid input. Please try again.")
        print()

def welcome_message():
    print("Welcome to the Count Unique Names CLI")
    print("You can run automated tests, run manual tests, and edit the maximum amount of typos allowed")
    print("Created by Chen Frydman")

def edit_max_typos():
    print("What is the new amount of typos allowed?")
    new_max_typos = int(input())
    if new_max_typos < 0:
        print("Max typos cannot be negative")
        return
    change_max_typos(new_max_typos)
    print(f"Max typos was updated to: {new_max_typos}")

def print_max_typos():
    print(f"Max typos allowed: {get_max_typos()}")

def run_all_tests():
    print("Running all automated tests")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    results = unittest.TextTestRunner(verbosity=2).run(test_suite)
    num_failures = len(results.failures)
    total = results.testsRun
    print(f"All tests complete. Tests run: {total}, Failures: {num_failures}, acceptance: {((total - num_failures)*100)/total}%")

def run_manual_test():
    print("Enter the first name on the billing address")
    billFirstName = input()
    print("Enter the last name on the billing address")
    billLastName = input()
    print("Enter the first name on the shipping address")
    shipFirstName = input()
    print("Enter the last name on the shipping address")
    shipLastName = input()
    print("Enter the name on the card")
    billNameOnCard = input()
    print(f"Expected Amount of unique names:")
    expected = int(input())
    try:
        if expected < 0:
            raise Exception("Expected result cannot be negative")
        amount_of_unique_names = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard)
        print(f"Manual test input: {billFirstName} {billLastName} {shipFirstName} {shipLastName} {billNameOnCard}")
        print(f"Manual test output: {amount_of_unique_names}")
        status = "PASS" if amount_of_unique_names == expected else "FAIL"
        print(f"{status}! Manual test output: {amount_of_unique_names}, expected: {expected}")
    except Exception as e:
        print(f"Error: {e}")

def print_menu():
    print("1. Edit Max Typos")
    print("2. Print Max Typos")
    print("3. Run All Tests")
    print("4. Run Manual Test")
    print("0. Exit")

if __name__ == "__main__":
    menu()