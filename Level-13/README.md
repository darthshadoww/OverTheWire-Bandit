# OverTheWire Bandit: Level 13

### Walkthrough
A total shift in strategy. I found a private SSH key (sshkey.private) instead of a password. I learned that passwords aren't the only way to authenticate. I used 'ssh -i sshkey.private' to log in to the next user directly.
chmod = Changes files restriction rules. Whether or not you can see.
			   Admin / Group / Others
	chmod 600 = rw-  ---      ---
	chmod 743 = rwx  r--      -wx

	ssh -i /Documents/bandit14 -p2220 bandit14@bandit.labs.overthewire.org

### What I Learned
* Asymmetric Cryptography. I understood how private/public key pairs work for secure server access without typing passwords.
