# Level 05: The Needle in the Haystack

### How I Found It
This was the first time I felt like a real 'searcher.' Thousands of files. I had to read the **documentation for `find`** (`man find`) very carefully. I filtered by size (1033 bytes), made sure it wasn't executable, and set it to human-readable. It was a great exercise in using complex command flags.

### The Solution
`find . -type f -size 1033c ! -executable`
