import itertools

# Customize based on victim information
first_name = "john"
last_name = "doe"
dob = "1990"

common_words = [first_name, last_name, dob, first_name + dob, last_name + dob, dob + first_name, dob + last_name]
special_chars = ["!", "@", "#", "123", "2024"]

passwords = set(common_words)

# Generate combinations with special characters
for word in common_words:
    for char in special_chars:
        passwords.add(word + char)
        passwords.add(char + word)

# Save to file
with open("personalized_passwords.txt", "w") as file:
    for pwd in passwords:
        file.write(pwd + "\n")

print("Generated", len(passwords), "passwords.")
