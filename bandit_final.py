import os
import subprocess
from datetime import datetime

# --- CONFIGURATION ---
REPO_PATH = os.path.expanduser("~/Documents/OverTheWire-Bandit")
START_DATE = "2026-05-06" # When your "every 2 days" timer starts

# This dictionary contains the "Humanish" content for your READMEs
LEVEL_CONTENT = {
    12: {
        "text": "This level was a nightmare of nested compression. I started with a hex dump in data.txt and had to use 'xxd -r' to turn it back into a binary. From there, it was a repetitive loop of checking file types with 'file' and decompressing using gzip, bzip2, and tar. It felt like opening a Russian Matryoshka doll made of data.",
        "learned": "Data Serialization and File Signatures. I learned how to reconstruct files from hex dumps and identify compression formats manually."
    },
    13: {
        "text": "A total shift in strategy. I found a private SSH key (sshkey.private) instead of a password. I learned that passwords aren't the only way to authenticate. I used 'ssh -i sshkey.private' to log in to the next user directly.",
        "learned": "Asymmetric Cryptography. I understood how private/public key pairs work for secure server access without typing passwords."
    },
    14: {
        "text": "My first real taste of networking. I had to submit the current level's password to a specific port (30000) on localhost to get the next one. I used Netcat (nc) to 'talk' to the service directly.",
        "learned": "Network Sockets. I learned how to interact with services on specific ports using the command line."
    },
    15: {
        "text": "Similar to the last one, but with encryption. The service at port 30001 uses SSL/TLS. I had to use 'openssl s_client' to establish a secure handshake before I could send the password.",
        "learned": "SSL/TLS Handshakes. I learned how to use OpenSSL to debug encrypted network connections."
    },
    16: {
        "text": "I played detective here. I used nmap to scan ports 31000-32000 to find an SSL service. Once found, I submitted the password and got an RSA key. I had to fix the file permissions with 'chmod 600' before the system would let me use the key to log in.",
        "learned": "Port Scanning and Permission Hardening. I learned about nmap and why SSH keys must have strict permissions."
    },
    17: {
        "text": "This was a lesson in spotting differences. I had two files, passwords.old and passwords.new. Instead of reading them, I used the 'diff' command to find the one line that changed.",
        "learned": "File Comparison. I learned how to efficiently find changes in configuration files using 'diff'."
    },
    18: {
        "text": "The 'Shell Jail' level. The server kicked me out immediately on login. I realized the .bashrc was modified. I bypassed it by sending the 'cat readme' command directly through the SSH connection string.",
        "learned": "SSH Command Execution. I learned you can run commands on a remote server without opening an interactive shell."
    },
    19: {
        "text": "I explored 'setuid' binaries. I found a program that runs with the permissions of bandit20. By running it, I could read the password file that was otherwise restricted.",
        "learned": "Privilege Escalation. I learned how SUID bits allow a user to execute a file with the permissions of the file owner."
    },
    20: {
        "text": "This was a two-way connection challenge. I set up a listener on one terminal using 'nc -l' and then ran a setuid program that connected back to it to exchange the password.",
        "learned": "Inter-Process Communication (IPC). I learned how two programs on the same machine can communicate over a local port."
    },
    21: {
        "text": "Introduction to Cron Jobs. I found a script in /etc/cron.d/ that was running every minute. I read the script to see where it was writing the next password.",
        "learned": "Linux Task Scheduling. I learned how to investigate automated background tasks using Cron."
    },
    22: {
        "text": "This was about script analysis. I found a shell script that generated a password based on a hash of the username. I figured out the logic and ran the command for bandit23 to get the key.",
        "learned": "Shell Script Deconstruction. I learned how to read and reverse-engineer basic bash logic."
    },
    23: {
        "text": "I had to write my own script! I placed a shell script in a folder that a cron job was monitoring. The cron job executed my script, which then copied the password to a place I could read it.",
        "learned": "Script Automation. I learned how to leverage existing automated tasks to run my own custom code."
    },
    24: {
        "text": "Time for Brute Forcing. I had to guess a 4-digit PIN. Instead of doing it by hand, I wrote a 'for' loop in bash to send every combination from 0000 to 9999 to the server port.",
        "learned": "Bash Scripting Loops. I learned how to automate repetitive input tasks using simple code."
    },
    25: {
        "text": "Breaking out of a restricted shell. The shell was set to 'more', which exits if the window is too big. I shrunk my terminal, triggered 'more', then used 'v' to open Vim and ':set shell=/bin/bash' to escape.",
        "learned": "Restricted Shell Escapes. I learned that many text viewers (like more/less) have 'backdoors' to the system shell."
    },
    26: {
        "text": "This was a continuation of the shell escape. I learned that even the login process is just a program that can be interrupted or manipulated if you know the right triggers.",
        "learned": "Linux Login Architecture. I understood how shells are assigned to users in /etc/passwd."
    },
    27: {
        "text": "Introduction to Git. I had to clone a repository from a local path. I used 'git clone' to bring the project files into a temporary directory.",
        "learned": "Version Control Basics. I learned how to clone repositories and navigate the Git file structure."
    },
    28: {
        "text": "Finding hidden data in Git logs. The password wasn't in the current file, so I looked at the history using 'git log -p'. I found the password in a previous commit where it had been 'deleted'.",
        "learned": "Git History. I learned that 'deleted' data in Git is never truly gone as long as the history exists."
    },
    29: {
        "text": "Working with Git branches. The password wasn't on the 'master' branch. I used 'git branch -a' to find other branches and 'git checkout' to switch to the one containing the secret.",
        "learned": "Git Branching. I learned how to navigate different versions of a project simultaneously."
    },
    30: {
        "text": "Git Tags. The password was hidden in a tag. I used 'git tag' to see the list and 'git show' to inspect the data inside the secret tag.",
        "learned": "Git Metadata. I learned that tags are often used to mark specific milestones or, in this case, hide secrets."
    },
    31: {
        "text": "Pushing to Git. I had to create a new file, add it, and push it back to the remote repository to trigger a response that gave me the password.",
        "learned": "The Git Workflow. I mastered the 'add-commit-push' cycle which is essential for every developer."
    },
    32: {
        "text": "The 'Upper Case' shell. Every command I typed was converted to uppercase, making them invalid. I realized that the shell variable '$0' referred to the shell itself. Running it broke me out into a normal session.",
        "learned": "Environment Variables. I learned how the shell handles input and how to use built-in variables to my advantage."
    },
    33: {
        "text": "The final level! This was a moment of reflection. I used all the skills—file navigation, grep, and permission checking—to find the final flag.",
        "learned": "Holistic Security. I realized that security isn't one tool, but a combination of understanding permissions, networking, and logic."
    },
}

def create_level_files(level_num):
    data = LEVEL_CONTENT[level_num]
    folder_name = f"Level-{level_num:02d}"
    folder_path = os.path.join(REPO_PATH, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# OverTheWire Bandit: Level {level_num}\n\n")
        f.write(f"### Walkthrough\n{data['text']}\n\n")
        f.write(f"### What I Learned\n* {data['learned']}\n")
    
    return folder_name

def run_git(msg):
    try:
        subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", msg], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "push"], cwd=REPO_PATH, check=True)
        print("Successfully updated GitHub!")
    except Exception as e:
        print(f"Git failed: {e}. (Make sure your Token is saved!)")

def main():
    mode = input("Type 'BULK' to finish all levels now, or 'AUTO' for the 2-day timer: ").strip().upper()
    
    if mode == "BULK":
        for lvl in range(12, 34):
            create_level_files(lvl)
        run_git("Complete Bandit Walkthrough: Levels 12-33")
    
    elif mode == "AUTO":
        start = datetime.strptime(START_DATE, "%Y-%m-%d")
        days_passed = (datetime.now() - start).days
        current_lvl = 12 + (days_passed // 2)
        
        if current_lvl in LEVEL_CONTENT:
            name = create_level_files(current_lvl)
            run_git(f"Automated Update: {name}")
        else:
            print("Already finished or no level scheduled for today.")

if __name__ == "__main__":
    main()
