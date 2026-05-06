# OverTheWire Bandit: Level 19

### Walkthrough
I explored 'setuid' binaries. I found a program that runs with the permissions of bandit20. By running it, I could read the password file that was otherwise restricted.

### What I Learned
* Privilege Escalation. I learned how SUID bits allow a user to execute a file with the permissions of the file owner.
