import math


def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius.
    """
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = math.pi * (radius ** 2)
        return area


# Get input from the user
try:
    user_radius = float(input("Enter the radius of the circle: "))

    # Calculate and display the area
    result = calculate_circle_area(user_radius)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The area of the circle with radius {user_radius} is: {result:.2f}")

except ValueError:
    print("Invalid input. Please enter a numerical value for the radius.")
else:
    print("error");