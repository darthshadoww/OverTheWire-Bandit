# OverTheWire Bandit: Level 13

### Walkthrough
A total shift in strategy. I found a private SSH key (sshkey.private) instead of a password. I learned that passwords aren't the only way to authenticate. I used 'ssh -i sshkey.private' to log in to the next user directly.

### What I Learned
* Asymmetric Cryptography. I understood how private/public key pairs work for secure server access without typing passwords.
