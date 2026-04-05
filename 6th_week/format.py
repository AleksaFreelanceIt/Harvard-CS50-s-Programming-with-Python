import re

name = input("What's your name?").strip()

if match := re.search(r"^(.+), *(.+)$", name):
    name = match.group(2) + " " + match.group(1)
print(f"hello, {name}")