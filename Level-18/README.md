# 🚩 OverTheWire Bandit: Level 18 → 19

### 📝 Level Objective
The goal is to retrieve the password from a file named `readme` in the home directory. However, the server is configured to kick you out (close the connection) immediately upon login. This is a classic "Shell Jail."

---

### 🛠️ The Solution: Bypassing the Login Shell
Since the `.bashrc` or login script is modified to force an exit, we cannot establish an interactive session. The trick is to send a command **directly** through the SSH connection. SSH executes the command and sends the output back before the "kick out" script can trigger.

**The Command:**
```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org "cat readme"
```

> **Note:** Using `"vim readme"` also works because it opens a separate environment, but `cat` is the cleanest way to grab the flag and exit.

**Next Level Password:** `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

---

### 🧠 Deep Dive: What is Bash?
**Bash (Bourne Again Shell)** is a **Command Line Interpreter (CLI)**. It takes your typed commands and explains them to the Operating System.

#### The "Car" Hierarchy
As you noted, the terminal and the shell are not the same thing. Think of it like this:
* **Hardware:** The Car.
* **Kernel:** The Engine (The core power).
* **OS:** The Driver's License (The rules and system).
* **Shell (Bash):** The Driver's Seat (Where the input happens).
* **Terminal:** The Gas Pedal and Stick (The physical interface you touch).

<img width="1148" height="687" alt="image" src="[https://github.com/user-attachments/assets/a3b1cfd8-f11e-4cc8-995a-071ca2116a9d](https://github.com/user-attachments/assets/a3b1cfd8-f11e-4cc8-995a-071ca2116a9d)" />

#### Other Shells:
* **`sh`**: The original ancestor.
* **`zsh`**: Improved version (default on many modern systems).
* **`fish`**: Friendly and modern.
* **`dash`**: Lightweight and fast.

---

### 📂 Understanding `.bashrc` and Hidden Files

A quick technical clarification:
* **`~/`**: This refers to your **Home Directory** (e.g., `/home/bandit18`).
* **`.` (The Dot Prefix)**: This is what makes a file **hidden**. Files like `.bashrc` are hidden by default and only show up with `ls -a`.

#### When does Bash execute?
Bash reads different scripts depending on how you enter the room:
1.  **Interactive Login Shell (SSH):** Looks for `/etc/profile` then `~/.bash_profile` or `~/.profile`.
2.  **Interactive Non-Login Shell (New Terminal Tab):** Reads `~/.bashrc`.

<img width="1259" height="751" alt="image" src="[https://github.com/user-attachments/assets/050749a7-6fc8-4b15-9e42-cff815a0a02c](https://github.com/user-attachments/assets/050749a7-6fc8-4b15-9e42-cff815a0a02c)" />

---

### 🔍 System Observations

#### Terminal Color Coding
While exploring, the colors in your terminal help identify what you're looking at:
* **Blue:** Directories (Folders).
* **White:** Standard Files.
* **Cyan:** **Symbolic Links** (Shortcuts/Pointers to other paths).

<img width="1259" height="751" alt="image" src="[https://github.com/user-attachments/assets/96fcd7db-ea1a-4bb4-9295-fc4a02c431f0](https://github.com/user-attachments/assets/96fcd7db-ea1a-4bb4-9295-fc4a02c431f0)" />

#### Permissions & The "Boss"
Inside `/etc/profile`, scripts often check if you are the root user. 
* **`#`**: Root/Admin (The Boss).
* **`$`**: Standard User.

<img width="1259" height="751" alt="image" src="[https://github.com/user-attachments/assets/64a9442e-10b4-48c9-aab2-e3258e0f99ba](https://github.com/user-attachments/assets/64a9442e-10b4-48c9-aab2-e3258e0f99ba)" />

---

### 💡 What I Learned
* **SSH Command Execution:** You can run commands on a remote server without ever opening an interactive shell prompt.
* **Shell Environments:** The difference between login and non-login shells and how they decide which configuration files to run.
* **Linux File Types:** Recognizing Symbolic Links and hidden configuration files.

