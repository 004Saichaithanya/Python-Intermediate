#Q10
import sys
s1 = sys.stdin.read()  # Reads all input until EOF (Ctrl+D in most terminals)
words =lines=ch = 0

for x in s1:
    if x:
        ch += 1
    if x == " ":
        words += 1
    if x == "\n":
        lines += 1
        words += 1  # Assuming each new line ends a word

# Output the counts
print("Characters:", ch)
print("Words:", words)
print("Lines:", lines)
