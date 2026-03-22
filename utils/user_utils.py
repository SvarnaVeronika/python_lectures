from utils.math_utils import add

def greet_user(username):
    print("Hello, " + username + "!")

def user_bye(username):
    print("Bye, " + username + "!")

def count_users(username):
    pass

def user_add(username, num1, num2):
    result = add(num1, num2)
    print(f"Uzivatel {username} scital cisla a vyslo mu {result}")
