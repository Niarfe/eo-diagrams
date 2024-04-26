import sys
import yaml
import json

template_top  = """<html>
  <body>
    ERD from schema.yml:
    <pre class="mermaid">
"""
template_bot = """
    </pre>

    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({ startOnLoad: true });
    </script>
  </body>
</html>
"""
assert len(sys.argv) == 2, "pass in path to schema.rb in yaml format"

data_loaded = None
with open(sys.argv[1], 'r') as stream:
    data_loaded = yaml.safe_load(stream)


fkeys = data_loaded['foreign_keys']
#print(json.dumps(fkeys, indent=4))
print(template_top)
print("erDiagram")

for fkey, relations in fkeys.items():
    for relation in relations:
        target, key = relation.split(':')
        print(fkey, "||--||", key, ":", target)

print(template_bot)





