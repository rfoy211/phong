import turtle

# Function to get full name from user input
def get_full_name():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    full_name = first_name + " " + last_name
    print("Your full name is", full_name)

# Function to capitalize input string
def capitalize_input():
    user_input = input("Your input: ")
    capitalized_input = user_input.upper()
    print("Capitalized:", capitalized_input)

# Function to square a number
def square_number():
    number = float(input("Input a number: "))
    squared_input = number ** 2
    print("Squared input:", squared_input)

# Function to draw a circle with custom radius
def draw_circle_with_radius():
    radius = float(input("Input circle's radius: "))
    turtle.circle(radius)
    turtle.done()

# Main function
def main():
    print("1. Full name\n")
    get_full_name()
    print("\n2. Capitalized name\n")
    capitalize_input()
    print("\n3. Square number\n")
    square_number()
    print("\n4. Turtle with custom radius\n")
    draw_circle_with_radius()

# Run the main function
if __name__ == "__main__":
    main()
