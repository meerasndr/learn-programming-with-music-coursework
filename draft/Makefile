
.PHONY: build
build:
	python3 src/build.py

serve: build
	python3 -m http.server --directory build/
