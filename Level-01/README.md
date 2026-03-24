# Level 01: The Mystery of the Dash

### How I Found It
I saw a file named `-`. My first instinct was `cat -`, but the terminal just sat there. I realized the shell interprets a single dash as 'read from stdin.' I searched StackOverflow and realized I needed to specify the path explicitly (`./-`) to tell the command it's a file, not an argument.

### The Solution
`cat ./- `
