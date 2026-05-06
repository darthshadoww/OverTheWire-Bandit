# OverTheWire Bandit: Level 16

### Walkthrough
I played detective here. I used nmap to scan ports 31000-32000 to find an SSL service. Once found, I submitted the password and got an RSA key. I had to fix the file permissions with 'chmod 600' before the system would let me use the key to log in.

### What I Learned
* Port Scanning and Permission Hardening. I learned about nmap and why SSH keys must have strict permissions.
