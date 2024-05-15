# Mastering using mermaidjs cli
We don't need to use local files anymore, mermaidjs provides a cli.

## Requisites
* Latest node, updated via `brew install node` and am using v22.x

## Install mermaid cli
* `npm install -g @mermaid-js/mermaid-cli`

## Example use
Using the example mindmap file, generate a png
* `mmdc -i example_mindmap.mmd -o output.png`
* It should generate a viewable output.png

## Next steps
* Refactor this to have makefile install stuff
* Our conversion then could be to include the png in a full webpage
* See the new `do/serve.py` for a way to pop up a server to serve those pages (light Flask) 


### Sources
* [mermaid-cli repo](https://github.com/mermaid-js/mermaid-cli)
* [mermaid site](https://mermaid.js.org/)
* [github repo](https://github.com/mermaid-js/mermaid)

[LINK TO HEADQUARTERS]( https://github.com/Niarfe/my_simple_notebook/tree/main)
