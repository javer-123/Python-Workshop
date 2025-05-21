def get_numbers_from_user():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def main():
    print("Enter numbers to calculate their sum.")
    numbers = get_numbers_from_user()
    total_sum = calculate_sum(numbers)
    print(f"The sum of the numbers is: {total_sum:.2f}")
if _name_ == "_main_":
     main()
