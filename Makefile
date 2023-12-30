.PHONY: coverageWebServer
coverageWebServer:
	cd tests/htmlcov && python3 -m http.server 8000
