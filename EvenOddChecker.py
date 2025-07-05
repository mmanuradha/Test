# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# --- Part 1: Check a single number ---
num = int(input("Enter a number to check if it is even or odd: "))
print(f"The number {num} is {check_even_odd(num)}.")

# --- Part 2: Check a list of numbers ---
numbers = [10, 23, 45, 66, 91, 100]  # You can change this list

print("\nChecking a list of numbers:")
for n in numbers:
    print(f"{n} is {check_even_odd(n)}.")
