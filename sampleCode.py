class Account:
    def __init__(self, owner, balance, pin):
        # 1. Public Attribute: Accessible directly and externally.
        self.owner = owner

        # 2. Protected Attribute: Indicated as internal/subclass use only.
        self._balance = balance

        # 3. Private Attribute: Name-mangled to prevent external access.
        self.__pin_code = pin

    def get_public_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance (Protected): {self._balance}")

    def get_pin(self):
        # Private attribute can be accessed internally by a public method
        print(f"PIN (Private): {self.__pin_code}")


# ----------------------------------------------------
# INSTANTIATION AND EXTERNAL ACCESS
# ----------------------------------------------------

my_account = Account("Alice", 5000, 1234)
print("\n--- Accessing Members from Outside the Class ---")

# 1. Public Access (Directly accessible and modifiable)
print(f"Public Access (Owner): {my_account.owner}")
# my_account.owner = "Bob" # Modification is easy
# print(f"Public (Modified Owner): {my_account.owner}")

# 2. Protected Access (Can be accessed, but shouldn't be, according to convention)
# Python lets you do this, but you shouldn't.
print(f"Protected Access (Balance): {my_account._balance}")
# my_account._balance = 6000
# try:
#     print(f"Private Access (balance): {my_account._balance}")
# except AttributeError as e:
#     print(f"Private Access Failed: {e}")
# 3. Private Access (Direct access attempt fails)
try:
    print(f"Private Access (PIN): {my_account.__pin_code}")
except AttributeError as e:
    print(f"Private Access Failed: {e}")

# Accessing the Private attribute via an internal (public) method:
print("\n--- Accessing Private via Internal Method ---")
my_account.get_pin()

print(my_account.get_public_info())