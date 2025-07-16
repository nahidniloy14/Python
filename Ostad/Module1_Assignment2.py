"""
Write a function to make an hour-to-minute converter.
"""
def convert_hours_to_minutes():
    # Ask the user to enter hours
    hours = input("Enter number of hours: ")

    # Convert input to an integer
    hours = int(hours)

    # Multiply by 60 to get minutes
    minutes = hours * 60

    # Print the result
    print(f"{hours} hour(s) is equal to {minutes} minute(s).")

# Call the function
convert_hours_to_minutes()
