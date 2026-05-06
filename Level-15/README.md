# OverTheWire Bandit: Level 15

### Walkthrough
Similar to the last one, but with encryption. The service at port 30001 uses SSL/TLS. I had to use 'openssl s_client' to establish a secure handshake before I could send the password.

### What I Learned
* SSL/TLS Handshakes. I learned how to use OpenSSL to debug encrypted network connections.
