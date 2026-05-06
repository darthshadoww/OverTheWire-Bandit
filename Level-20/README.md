# OverTheWire Bandit: Level 20

### Walkthrough
This was a two-way connection challenge. I set up a listener on one terminal using 'nc -l' and then ran a setuid program that connected back to it to exchange the password.

### What I Learned
* Inter-Process Communication (IPC). I learned how two programs on the same machine can communicate over a local port.
