import requests
import time

# Our own local demo website
LOGIN_URL = "http://127.0.0.1:5000/login"

print("Starting password test...")
print("Testing passwords from 000 to 999\n")

for number in range(1000):
    password = f"{number:03d}"

    response = requests.post(
        LOGIN_URL,
        json={"password": password},
        timeout=5
    )

    result = response.json()

    print(f"Trying: {password}")

    if response.ok and result.get("success") is True:
        print("\nPassword found!")
        print(f"Correct password: {password}")
        break

    time.sleep(0.02)

else:
    print("\nNo correct password found.")