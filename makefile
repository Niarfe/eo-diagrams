default:
	@cat makefile

install:
	npm install -g @mermaid-js/mermaid-cli

html:
	python3 generate.py ${SOURCE} > src/${SOURCE}.mer
	do/eo-diag.py src/${SOURCE}.mer

mer2html:
	do/eo-diag.py src/${SOURCE}


