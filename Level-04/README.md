# Level 04: The Human Factor

### How I Found It
A directory full of binary-looking files. I didn't want to `cat` them all and mess up my terminal's encoding. I used the `file` command on every file in the directory to let the system tell me which one was actually ASCII text.

### The Solution
`file ./*` then read the one labeled 'ASCII text'.
