import time, os


def get_celcius(user_input):
    """
    Generates a new image by calling the PRNG Service and Image Service.

    Returns:
        str: The path to the generated image.
    """
    fahrenheit = user_input
    # Call the Celcius Service
    with open("fahrenheit-to-celcius.txt", "w") as file:
        file.write(fahrenheit)

    time.sleep(5)  # Wait for the Celcius Service to convert the number

    # Read the converted temperature from the Celcius Service
    with open("fahrenheit-to-celcius.txt", "r") as file:
        celcius = file.read().strip()

    return celcius


def main():
    """
    Main function that runs the user interface loop.
    """
    while True:
        user_input = input("Enter temperature in Fahrenheit: ")

        if user_input.isdigit():
            celcius = get_celcius(user_input)
            print(f"Temperature in Celcius: {celcius}")
        else:
            print("Unknown option. Please try again.")


if __name__ == "__main__":
    main()