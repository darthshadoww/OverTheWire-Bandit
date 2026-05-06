# OverTheWire Bandit: Level 25

### Walkthrough
Breaking out of a restricted shell. The shell was set to 'more', which exits if the window is too big. I shrunk my terminal, triggered 'more', then used 'v' to open Vim and ':set shell=/bin/bash' to escape.

### What I Learned
* Restricted Shell Escapes. I learned that many text viewers (like more/less) have 'backdoors' to the system shell.
