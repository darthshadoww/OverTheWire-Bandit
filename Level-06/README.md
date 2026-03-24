# Level 06: System-Wide Search

### How I Found It
The file was 'somewhere on the server.' Searching the root directory (`/`) results in a massive amount of 'Permission Denied' errors. I used the trick of redirecting `stderr` to `/dev/null` so I could actually see the one successful result.

### The Solution
`find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`
