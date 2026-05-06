# OverTheWire Bandit: Level 15

### Walkthrough
This level is a direct evolution of Level 14. While the previous level used a "cleartext" connection, the service at port **30001** requires a secure connection using **SSL/TLS**. 

If you try to use `nc` (Netcat) here, the connection will fail because Netcat doesn't know how to perform the "Handshake" required to encrypt the data. Instead, I used `openssl s_client` to wrap the communication in a secure tunnel.

* <img width="433" height="460" alt="image" src="https://github.com/user-attachments/assets/f38e5cb8-b0f4-4f32-b0c8-83188504d127" />


### Core Concepts: SSL vs. TLS
*   **SSL (Secure Sockets Layer):** The original protocol for encrypting web traffic. It is now considered deprecated (obsolete).
*   **TLS (Transport Layer Security):** The modern, more secure successor to SSL. Even though most people still say "SSL," they are almost always using TLS.

#### The Three Pillars of Security
SSL/TLS provides three essential protections:
1.  **Encryption:** Scrambles the data so "Man-in-the-Middle" observers cannot read it.
2.  **Authentication:** Uses certificates to prove the server is who they claim to be.
3.  **Integrity:** Uses checksums to ensure the data wasn't tampered with during transit.

---

### Tools: OpenSSL `s_client`
Think of `openssl s_client` as **"Netcat with a Bulletproof Vest."** It allows you to connect to a remote host using SSL/TLS encryption.

**The Command:**
```bash
openssl s_client -connect [host]:[port]
```
*   **`-connect`**: This flag is required to specify the destination.
*   **The Handshake**: After running this, you will see a lot of text regarding certificates. Once you see `DONE` or a prompt, the "Secure Tunnel" is open, and you can paste your password.

> **Note on "Read R Block":** When you see a "Read R" or session block in the output, it indicates the secure session parameters (like the Cipher Suite used) have been established and recorded.

---

### What I Learned
*   **Encrypted Sockets:** Not all ports accept raw text; many require a cryptographic handshake first.
*   **Protocol Evolution:** Understanding that TLS is the current standard for securing data in transit.
*   **OpenSSL Basics:** Using `s_client` to debug and interact with encrypted services.


