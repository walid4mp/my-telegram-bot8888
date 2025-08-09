import os
import requests
import time
import random
import webbrowser

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Emoji list
emojis = ['📞', '📲', '☎️', '🔔', '📢', '📡', '⏰', '📳', '🛎️']

def rand_emoji():
    return random.choice(emojis)

def speak(text):
    os.system(f'espeak -a 100 "{text}"')
	os.system('xdg-open https://t.me/sabitcommunity')

def banner():
    print(f"""{CYAN}
__  __ ____    ____    _    ____ ___ _____ 
|  \/  |  _ \  / ___|  / \  | __ )_ _|_   _|
| |\/| | |_) | \___ \ / _ \ |  _ \| |  | |  
| |  | |  _ <   ___) / ___ \| |_) | |  | |  
|_|  |_|_| \_\ |____/_/   \_\____/___| |_|  
{RESET}{YELLOW}
    CALL-BOOMBER  BY MR_SABIT{rand_emoji()}
       TELEGRAM    : SABIT_x{rand_emoji()}
       TOOL        : FREE{rand_emoji()}
       VERSION     : 0.1 {rand_emoji()}
       
{RESET}""")
    speak("Welcome to call bomber tool")

def send_call_boom(number, count):
    url = f""  # 🔴 এখানে তোর API বা URL বসাতে হবে
    for i in range(count):
        emoji = rand_emoji()
        try:
            response = requests.get(url)
            if response.status_code == 200 and 'success' in response.text.lower():
                print(f"{GREEN}[✓] Call {i + 1} sent to {number} successfully! {emoji}{RESET}")
            else:
                print(f"{RED}[×] Call {i + 1} failed or no actual call sent. {emoji}{RESET}")
        except Exception as e:
            print(f"{RED}[!] Error: {e} {emoji}{RESET}")
        time.sleep(1)

def open_telegram_group():
    webbrowser.open("https://t.me/sabitcommunity")
    speak("Please join our Telegram group to continue " + rand_emoji())

def is_user_in_group():
    print(f"{YELLOW}Join the Telegram group: https://t.me/sabitcommunity {rand_emoji()}{RESET}")
    input(f"{CYAN}After joining, press Enter to continue... {rand_emoji()}{RESET}")
    return True

def main():
    os.system('clear')
    banner()

    if not is_user_in_group():
        print(f"{RED}You must join the Telegram group first! Redirecting... {rand_emoji()}{RESET}")
        open_telegram_group()
        return

    print(f"{CYAN}Enter victim number (e.g. +8801xxxxxxxxx): {RESET}{rand_emoji()}")
    number = input("> ")

    speak("Enter victim number " + rand_emoji())

    try:
        total_calls = int(input(f"{CYAN}How many calls to send: {RESET}{rand_emoji()}"))
    except:
        total_calls = 10
        print(f"{YELLOW}Invalid input! Defaulting to 10 calls. {rand_emoji()}{RESET}")
        speak("Starting call bombing " + rand_emoji())

    print(f"{YELLOW}Starting call boom on {number}... {rand_emoji()}{RESET}")
    send_call_boom(number, total_calls)
    speak("Call bombing complete " + rand_emoji())
    print(f"{GREEN}Done! All calls attempted. {rand_emoji()}{RESET}")

if __name__ == "__main__":
    main()