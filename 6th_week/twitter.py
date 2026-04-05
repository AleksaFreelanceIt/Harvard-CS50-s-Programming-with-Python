import re
url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?x\.com/", "", url)
#print(f"Username: {username}")

if match := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", match.group(1))