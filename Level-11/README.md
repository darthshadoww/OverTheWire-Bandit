# Level 11: The Secret Shift

### How I Found It
This level was about ROT13. I recognized the pattern (shifted alphabet). I used the `tr` (translate) command to map the entire alphabet 13 places forward. It felt like solving a classic cryptogram.

### The Solution
`cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
