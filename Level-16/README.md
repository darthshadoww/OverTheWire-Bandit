This level is where you really start acting like a penetration tester. You’ve successfully moved from "talking to a known port" to "hunting for the right port" and managing cryptographic keys.

I've reorganized your notes to highlight the difference between scanning techniques and why that `chmod` command was so critical for your RSA key.

---

# OverTheWire Bandit: Level 16

### Walkthrough
In this level, I played detective. Instead of being given a port, I had to find it myself within a range of **31000 to 32000**. I used `nmap` to identify which ports were open and, more importantly, which one was running the SSL service that would give me the next credential.

After submitting the Level 15 password to the correct port, the server returned an **RSA Private Key**. To use this key for the next level, I had to manually create a file and set strict permissions using `chmod 600`—otherwise, SSH would reject it for being "too open."

---

### Deep Dive: Port Scanning with `nmap`
To find the right service, I used a multi-step scanning approach:

1.  **The Discovery Scan:** 
    `nmap -p 31000-32000 localhost`
    This identified several open ports, but didn't tell me what they were doing.

2.  **The Service Scan:**
    `nmap -p [ports] -sV localhost`
    By adding `-sV`, I asked `nmap` to determine the **version** and **service** type.
    *   **echo:** Just repeats what you say.
    *   **ssl/echo:** Secure, but still just an echo service.
    *   **ssl/unknown:** The target! This indicated a service waiting for specific input (our password).

<img width="467" height="476" alt="image" src="https://github.com/user-attachments/assets/05faace4-0081-4004-bd6f-3fe152a44f81" />


---

### Technical Theory: TCP Scans
Understanding how `nmap` talks to the server is key to being "stealthy."

#### The TCP Three-Way Handshake
A standard connection (`-sT`) completes the full handshake:
1.  **SYN:** "Hey, are you there?"
2.  **SYN-ACK:** "Yes, I am. Let's talk."
3.  **ACK:** "Great, here is my data."
<img width="843" height="463" alt="image" src="https://github.com/user-attachments/assets/d27a3f99-ae52-4fd8-b8c6-af35d5425ad7" />



#### The Stealth (SYN) Scan (`-sS`)
This is the "Half-Open" scan. It sends a **SYN**, waits for the **SYN-ACK** to confirm the port is open, and then immediately sends a **RST** (Reset) to close the connection before it's fully established. This often avoids being logged by basic application firewalls.
<img width="843" height="463" alt="image" src="https://github.com/user-attachments/assets/907c2a0f-782b-4e33-9915-fa176052c245" />

---

### Security Best Practice: RSA Key Permissions
When the server gave me the RSA Private Key, I saved it to a file (e.g., `private.key`). However, SSH is very picky about security:
*   If a private key is "world-readable," an attacker on the same system could steal it.
*   **The Fix:** `chmod 600 private.key`
*   This command ensures that **only the owner** can read or write the file. Without this, the command `ssh -i private.key bandit17@localhost` will fail.
<img width="1128" height="374" alt="image" src="https://github.com/user-attachments/assets/42f052a0-bf6f-4ed6-b488-6286b3b772a7" />

---
<img width="1245" height="585" alt="image" src="https://github.com/user-attachments/assets/4060ce8e-e197-4138-821a-60e6d9f93b13" />

### What I Learned
*   **Service Fingerprinting:** Using `-sV` to distinguish between "noise" (echo) and actual services.
*   **Stealth vs. Full Connect:** The mechanics of SYN scans vs. TCP Connect scans.
*   **Permission Hardening:** Why private keys must be protected with `600` permissions to be functionally valid in Linux.
