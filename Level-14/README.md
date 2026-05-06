# OverTheWire Bandit: Level 14

### Walkthrough
My first real taste of networking. I had to submit the current level's password to a specific port (30000) on localhost to get the next one. I used Netcat (nc) to 'talk' to the service directly.

FTP = File Transfer Protocol
	Port = Every machine makes itself availible in internet by using Ports
	most knowns ports are;
	80 =WWW
	21 = FTP
	7 = echo
	79 = finger
	43 = nicname (Who ls)
	Port numbers are created with TCP(Transmmission control protocol) and IP(Internet Protocol) 
	most common ports are TCP and UDP(User Datagram Protocol)

	Localhost = just a network inside of your machine for you, without requiring physical network interface. For testing stuffs
	so what's TCP UDP?
	TCP is like a registered letter, you send it and they confirm it. 
	UDP is more like a broadcast. you shout for the message, but if the listener misses a word, everyone misses.

	netcat = so it's an army swiss knife in linux. It's a tool that help us to connect to network. It's like a cat function in network.
	it works like this:
		nc [options] [hostname] [port]
		options are first letter of these;
			-listen
==(Remember! Server use this, client just connects without using any options.) f.e. nc 192.168.1.1 80==
			-verbose(describes speech)
			-port
			-z : scans for open ports
			-w: sets a timeout for connections
			-q : specifies dealy before connection
### What I Learned
* Network Sockets. I learned how to interact with services on specific ports using the command line.
