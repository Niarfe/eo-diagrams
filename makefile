default:
	@cat makefile

html:
	python3 generate.py ${SOURCE} > src/${SOURCE}.mer
	do/eo-diag.py src/${SOURCE}.mer

mer2html:
	do/eo-diag.py src/${SOURCE}


