# CymeraCrypt
CymeraCrypt is an educational ransomware project. It is unfinished however it will be live and working in the next few weeks.

## What it does:
Installs its dependencies (pycryptodome and paramiko) via pip.
Encrypts your files. It walks through the Downloads, Documents and Desktop folders. Each file is encrypted with AES-256 and saved with a .aes extension, and the original is deleted.
Tries to spread. It scans the local /24 network for machines with SMB (port 445) open and tries to copy itself over with PsExec, using the credentials Administrator / password.
Tries to open a reverse shell over SSH to an attacker’s server. The host and credentials are still placeholders (your_attacker_server), so this part doesn’t work as written.
Shows a ransom note. It claims the computer is locked, demands 1 BTC, and asks for a password. A wrong password triggers a forced Blue Screen of Death through a Windows API call.

### Issue (work in progress)
It’s amateur work, with copy-pasted placeholders, a hardcoded encryption key and a hardcoded unlock password, all visible in the source. The “Bitcoin address” is actually an extended public key (Zpub), so it isn’t a usable payment address.
Because the key is hardcoded, files encrypted by this exact sample could in principle be decrypted with it. That wouldn’t apply to real-world ransomware.
It’s still destructive. It deletes the originals and would do real damage on a real machine.
