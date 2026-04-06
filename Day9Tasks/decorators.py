# Decorator function
def login_required(func):
    def wrapper(user):
        if user == "admin":   # simple authentication check
            print("Access Granted")
            func(user)
        else:
            print("Access Denied. Please login first.")
    return wrapper


# Sensitive function
@login_required
def view_dashboard(user):
    print("Welcome to Dashboard,", user)


# Main function
def main():
    user1 = "admin"
    user2 = "guest"

    view_dashboard(user1)   # allowed
    view_dashboard(user2)   # denied


# Entry point
if __name__ == "__main__":
    main()
