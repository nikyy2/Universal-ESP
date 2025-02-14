import os 
os.system("pip install psutil")
os.system("pip install requests")
        
def find_roblox_process():
    global folder_path
    process_name = "RobloxPlayerBeta.exe"
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.info['name'] == process_name:
                exe_path = proc.info['exe']
                folder_path = os.path.dirname(exe_path)
                print("made by nikymetaa and Z.")
                return folder_path
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    else:
        print("⚠️ ❌ Error! Make sure Roblox is running.")
        
file_urls = {
    "1": ("Mode 1", 'https://raw.githubusercontent.com/nikyy2/Universal-ESP/refs/heads/main/smallcubeesp.mesh'),
    "2": ("Mode 2", 'https://raw.githubusercontent.com/nikyy2/Universal-ESP/refs/heads/main/HeadESPSmall.mesh'),
    "3": ("Mode 3", 'https://raw.githubusercontent.com/nikyy2/Universal-ESP/refs/heads/main/HeadESPLarge.mesh'),
    "4": ("Mode 4", 'https://raw.githubusercontent.com/nikyy2/Universal-ESP/refs/heads/main/HeadESPExtraLarge.mesh'),
    "0": ("No ESP", 'https://raw.githubusercontent.com/nikyy2/Universal-ESP/refs/heads/main/default.mesh')
}

def download_and_save_file(url, save_path):
    r = requests.get(url)
    if r.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(r.content)
    else:
        print(f"⚠️ ❌ Error. Please report this to NIKY!")

def show_main_menu():
    os.system("cls")
    print("======== made by nikyy2 & Z ========")
    print("Choose a mode:")
    print("------------------------------------------")
    for key, (name, _) in file_urls.items():
        print(f" {key}. {name}")
    print("------------------------------------------")
    choice = input("Enter your choice (1-4 or 0): ").strip()
    return choice

if __name__ == "__main__":
    import psutil, requests
    os.system("cls")
    find_roblox_process()
    
    if folder_path:
        while True:
            choice = show_main_menu()
            if choice in file_urls:
                _, file_url = file_urls[choice]
                save_path = f"{folder_path}/content/avatar/heads/head.mesh"
                download_and_save_file(file_url, save_path)
                print("\n✅ Ready to join the game!")
                continue_choice = input("\nDo you want to return to the main menu? (y/n): ").strip().lower()
                if continue_choice == 'y':
                    os.system("cls")
                else:
                    break
            else:
                print("⚠️ ❌ Invalid choice. Exiting...")
                break
