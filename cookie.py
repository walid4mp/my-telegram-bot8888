import requests

email = input("📧 Email/Phone: ")
password = input("🔑 Password: ")

login_url = "https://mbasic.facebook.com/login.php"
session = requests.Session()

data = {
    "email": email,
    "pass": password
}

res = session.post(login_url, data=data)

if "c_user" in session.cookies.get_dict():
    cookies = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
    print("\n✅ Your Cookie:\n")
    print(cookies)
else:
    print("\n❌ Login failed! Check your info.")
