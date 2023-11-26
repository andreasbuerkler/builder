.PHONY: all unittest coverageWebServer

all: coverageWebServer

unittest:
	cd test && coverage run -m unittest discover

coverageWebServer: unittest
	cd test/htmlcov && python3 -m http.server 8000

