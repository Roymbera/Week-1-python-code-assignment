
def get_user_info():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    location = input("Please enter your location: ")
    
    # Print the personalized message
    print(f"Hello {name}, you are {age} years old and live in {location}.")

if __name__ == "__main__":
    get_user_info()
