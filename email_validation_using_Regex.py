import re

email_condition = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
user_email = input("Enter your Email: ")

if re.fullmatch(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")
