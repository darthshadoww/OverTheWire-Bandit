# Level 10: Base64 Decryption

### How I Found It
The text looked like random gibberish but ended with an '='—a classic sign of Base64 encoding. I searched 'how to decode base64 in linux' and found the native tool.

### The Solution
`base64 -d data.txt`
