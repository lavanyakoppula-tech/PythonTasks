# Dictionary to store user roles
user_roles = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest"
}
# Decorator to check access
def access_control(required_role):
    def decorator(func):
        def wrapper(user):
            # Condition to check role
            if user in user_roles and user_roles[user] == required_role:
                return func(user)
            else:
                print(f"Access denied for {user}")
        return wrapper
    return decorator


# Applying decorator to multiple functions
@access_control("admin")
def delete_data(user):
    print(f"{user} deleted the data")


@access_control("user")
def view_data(user):
    print(f"{user} is viewing data")


@access_control("admin")
def modify_data(user):
    print(f"{user} modified the data")


# Using the functions
users = ["alice", "bob", "charlie"]

for u in users:
    print("\nUser:", u)
    view_data(u)
    delete_data(u)
    modify_data(u)
