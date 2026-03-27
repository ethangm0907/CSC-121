# 9-5. Login Attempts

class User:

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.login_attempts = 0   # new attribute

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name} ({self.username})")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

    # method to increase login attempts
    def increment_login_attempts(self):
        self.login_attempts += 1

    # method to reset login attempts
    def reset_login_attempts(self):
        self.login_attempts = 0


# create a user
user1 = User("Ethan", "Miller", "ethan123")

# increment login attempts multiple times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# print attempts
print("Login attempts:", user1.login_attempts)

# reset attempts
user1.reset_login_attempts()

# print again to confirm reset
print("Login attempts after reset:", user1.login_attempts)

Login attempts: 3
Login attempts after reset: 0
