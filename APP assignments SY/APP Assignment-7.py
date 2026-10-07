import re

text = "Contact us at abc@gmail.com or student123@yahoo.com for more information."

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print("Email addresses found:")
for email in emails:
    print(email)
    