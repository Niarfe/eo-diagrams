"""
Load a text file
Rewrite it with a html/body/pre tags
Open in Chrome
Remove intermediate file

Good for printing those big pesky text files
"""
import sys
import os

assert len(sys.argv) == 2, "Pass in file with plain text to open"

source = sys.argv[1]

with open('temp.html', 'w') as target:
    target.write('<html><body><pre>\n')
    text = open(source, 'r').read()
    target.write(text)
    target.write('\n</pre></body></html>')

os.system("open -a 'Google Chrome' temp.html; sleep 5; rm temp.html")
