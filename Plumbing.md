# Plumbing 1

## Solution
- Created a new file to redirect output called plumber.txt.  Used ncat command and -o option to dump data to a file.  When file contained data I used grep FS{ to find the flag.

<img width="863" alt="Screen Shot 2020-11-22 at 10 03 42 PM" src="https://user-images.githubusercontent.com/74154888/99926143-a1aa0b80-2d0e-11eb-9c7d-30f4998be3c5.png">

### Ncat
- ncat or nc is networking utility with functionality similar to cat command but for network. It  is a general purpose CLI tool for reading, writing, redirecting data across a network.

### Options
- -o Used with ncat and filename to dump session data into a file
- grep used to search for specified pattern separated by newline character and will print each line that matches the pattern
