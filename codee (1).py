import re
import requests
import base64
import os
import json
import subprocess
import uuid
import time

CONFIG_FILE = "config_rshoka.json"
APPROVED_FILE = "approved_ids.txt"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("\033[1;35m" + "="*56)
    print("  ██████╗ ██╗   ██╗██╗ █████╗ ██╗     ███████╗")
    print("  ██╔══██╗██║   ██║██║██╔══██╗██║     ██╔════╝")
    print("  ██████╔╝██║   ██║██║███████║██║     █████╗  ")
    print("  ██╔══██╗██║   ██║██║██╔══██║██║     ██╔══╝  ")
    print("  ██║  ██║╚██████╔╝██║██║  ██║███████╗███████╗")
    print("  ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝")
    print("="*56 + "\033[0m")
    print("\033[1;36m              TikTok Paing Gyi WiFi Bypass Tool\033[0m")

def get_hwid():
    try:
        cmd = "wmic cpu get processorid"
        return subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
    except:
        return "UNKNOWN_ID"

def check_internet():
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except:
        return False

def check_approval():
    hwid = get_hwid()
    if os.path.exists(APPROVED_FILE):
        with open(APPROVED_FILE, "r") as f:
            if hwid in f.read().splitlines():
                return True
    return False

def setup_wifi_config():
    if check_internet():
        print("\033[1;31m[!] Internet connection detected! Please turn off Wi-Fi/Data.\033[0m")
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        input("\nPress Enter to retry...")
        return

    clear_screen()
    banner()
    print("\033[1;33m[ 1 ] Setup WiFi Configuration\033[0m")
    url = input("Enter Portal URL: ")
    mac = input("Enter MAC Address: ")
    voucher = input("Enter Voucher Code: ")
    gateway = input("Enter Gateway IP: ")
    
    config = {"url": url, "mac": mac, "voucher": voucher, "gateway": gateway}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    
    print(f"\n[✓] Configuration saved successfully! Gateway: {gateway}")
    input("\n[✓] Press Enter to continue...")

def start_bypass():
    if not os.path.exists(CONFIG_FILE):
        print("\033[1;31m[!] Config not found. Please run Setup first!\033[0m")
        input("Press Enter to continue...")
        return
    
    sid = uuid.uuid4().hex
    print(f"\n[+] Inactive Session Id: {sid}")
    time.sleep(1)
    print(f"[+] Active Session Id: {sid}")
    
    print("\n\033[1;32m" + "📌" * 15)
    print("      INTERNET CONNECTED SUCCESSFULLY!")
    print("📌" * 15 + "\033[0m")
    input("\nPress Enter to return to menu...")

def main_menu():
    clear_screen()
    banner()
    if not check_approval():
        print(f"\nDevice ID: {get_hwid()}")
        print("\033[1;31m[-] Device not approved! Contact Admin.\033[0m")
        return
    
    print("\033[1;32m[ KEY APPROVED ]\033[0m")
    input("Press Enter to continue...")
    
    while True:
        clear_screen()
        banner()
        print(" [1] Setup WiFi (Config)")
        print(" [2] Start Internet Connection")
        print(" [3] Reset Saved Data")
        print(" [4] Exit")
        
        choice = input("\n=> Select option: ")
        if choice == "1":
            setup_wifi_config()
        elif choice == "2":
            start_bypass()
        elif choice == "3":
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            print("[✓] Data reset.")
            input()
        elif choice == "4":
            break

if __name__ == "__main__":
    main_menu()
    
