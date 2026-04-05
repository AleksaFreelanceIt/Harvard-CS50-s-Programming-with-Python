import re

email = input("What's your email? ").strip()

#if re.search(r"^.+@.+\.com$", email):
#    print("valid")
#else:
#    print("invalid")

if re.search(r"^[a-zA-Z0-9_]+@(\w+\.)?\w+\.(com|net|edu|gov|org)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")