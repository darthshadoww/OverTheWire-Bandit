# Level 09: Binary Scavenger

### How I Found It
The file was a binary mess. I used the `strings` command to extract everything that looked like human-readable text and then filtered for the '==' signature usually found near passwords in this game.

### The Solution
`strings data.txt | grep "=="`
