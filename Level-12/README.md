# OverTheWire Bandit: Level 12

### Walkthrough
This level was a nightmare of nested compression. I started with a hex dump in data.txt and had to use 'xxd -r' to turn it back into a binary. From there, it was a repetitive loop of checking file types with 'file' and decompressing using gzip, bzip2, and tar. It felt like opening a Russian Matryoshka doll made of data.

### What I Learned
* Data Serialization and File Signatures. I learned how to reconstruct files from hex dumps and identify compression formats manually.
