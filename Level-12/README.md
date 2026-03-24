# Bandit Level-12

Objective: Decompress nested hexdump.
Solution: `xxd -r data.txt > mystery` followed by repeated `file`, `gunzip`, `bzip2`, and `tar` commands.
Key Commands: xxd, gzip, bzip2, tar
