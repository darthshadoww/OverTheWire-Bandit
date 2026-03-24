# Level 12: The Matryoshka Doll

### How I Found It
This was the hardest level yet. A file compressed inside a file, inside a hexdump. I had to use `xxd -r` to turn it back into binary, then repeatedly used `file` to identify the compression (Gzip, Bzip2, Tar) and decompress it over and over. It took a lot of patience and renaming files.

### The Solution
Repeated use of `file`, `xxd`, `gunzip`, `bzip2 -d`, and `tar -xf`.
