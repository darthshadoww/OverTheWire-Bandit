# OverTheWire Bandit: Level 14

### Walkthrough
This level provided my first real taste of networking. To progress, I had to submit the password for the current level to a specific port (**30000**) on **localhost**. I used **Netcat (`nc`)** to "talk" to the service directly.

#### Core Networking Concepts
*   **Ports:** Think of an IP address as a building's street address and a **Port** as a specific door or mailbox. Every machine makes services available via these ports.
*   **Common Ports:**
    *   `21`: FTP (File Transfer Protocol)
    *   `43`: WHOIS (Nicname)
    *   `79`: Finger
    *   `80`: HTTP (World Wide Web)
*   **Protocol Layers:** Port numbers are used by **TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol), which sit on top of **IP** (Internet Protocol).

#### TCP vs. UDP
| Feature | TCP | UDP |
| :--- | :--- | :--- |
| **Analogy** | A registered letter (requires a signature/confirmation). | A megaphone broadcast (shouting into a crowd). |
| **Reliability** | High; confirms the data arrived intact. | Lower; fast, but doesn't check if data was received. |

#### Localhost
**Localhost** (`127.0.0.1`) is a loopback network interface. It allows a machine to communicate with itself for testing and internal services without needing an external physical network.

---

### Tools: Netcat (`nc`)
Netcat is often called the **"Swiss Army Knife"** of networking. It allows you to read from and write to network connections. Think of it as the `cat` command, but for the network.

**Basic Usage:**
`nc [options] [hostname] [port]`

**Common Flags:**
*   `-l`: **Listen** mode (used by servers to wait for incoming connections).
*   `-v`: **Verbose** (provides more detail about what the connection is doing).
*   `-p`: **Port** (specifies the source port).
*   `-z`: **Zero-I/O** (used for scanning open ports without sending data).
*   `-w`: **Wait** (sets a timeout for connections).

> **Remember:** A server uses `-l` to listen, while a client (like us in this level) simply connects:
> `nc localhost 30000`

---

### What I Learned
*   **Network Sockets:** I learned how to interact with services on specific ports using the command line.
*   **Client-Server Interaction:** The distinction between a service listening on a port and a client initiating a connection.
