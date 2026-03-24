# Level 08: Standing Out

### How I Found It
I needed a line that occurred only once. I read that `uniq` can find unique lines, but its **documentation** states it only works on *adjacent* lines. So, I piped the file into `sort` first, then into `uniq -u`.

### The Solution
`sort data.txt | uniq -u`
