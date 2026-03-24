# Level 00: The Entry Point

### How I Found It
I started by reading the level description which provided the hostname and port. Since I'm running **Arch Linux**, I simply opened my terminal and used the standard OpenSSH client. I had to ensure I specified the custom port `2220`, as standard SSH defaults to 22. Once connected, a quick `ls` showed the `readme` file.

### The Solution
`ssh bandit0@bandit.labs.overthewire.org -p 2220`
Password: `bandit0`
