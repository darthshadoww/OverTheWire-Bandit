# Level 03: Hiding in Plain Sight

### How I Found It
The `inhere` directory looked empty with a normal `ls`. I remembered from my early Linux labs that hidden files start with a dot. I checked the `man ls` page to find the flag for showing all entries.

### The Solution
`ls -la` then `cat .hidden`
