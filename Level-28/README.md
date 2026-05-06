# OverTheWire Bandit: Level 28

### Walkthrough
Finding hidden data in Git logs. The password wasn't in the current file, so I looked at the history using 'git log -p'. I found the password in a previous commit where it had been 'deleted'.

### What I Learned
* Git History. I learned that 'deleted' data in Git is never truly gone as long as the history exists.
