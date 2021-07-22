#!/usr/bin/env python3
import os
import sys

head = """<html>
    <head>
        <link href="css/mermaid.css" type="text/css" rel="stylesheet" />
        <!-- <script>mermaid.initialize({startOnLoad:true});</script> -->
    </head>
    <body>
<div class="mermaid">
"""

footer = """
</div>
    <script src="js/mermaid.min.js"></script>
    </body>
</html>
"""

if __name__ == "__main__":
    try:
        fname = sys.argv[1]
        bname = os.path.basename(os.path.splitext(fname)[0])
        output_name = "build/"+bname+".html"

    except:
        print("\n\tUsage: {} <sourcefile>".format(__file__))
        print("\tWhere sourcefile is a mermaid dsl text file\n")
        sys.exit(1)

    with open(fname, 'r') as source:
        print("Reading source", fname)
        mermaid_diagrame = source.read()

    with open(output_name, 'w') as target:
        target.write(head+"\n")
        target.write(mermaid_diagrame+"\n")
        target.write(footer)
        print("wrote to file", output_name)
