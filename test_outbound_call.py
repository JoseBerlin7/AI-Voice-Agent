import requests

BASE_URL = ""

TEST_NUMBER = ""

def test_make_call():
    try:
        print(f"Initiating call to {TEST_NUMBER}...")
        response = requests.get(f"{BASE_URL}/make_call/{TEST_NUMBER}")
        print("Status:", response.status_code)
        print("Response:", response.text)

        if response.status_code == 200:
            print("Call initiated successfully.")
        else:
            print("Something went wrong.")
    except Exception as e:
        print("Error caught :", str(e))

if __name__ == "__main__":
    test_make_call()
