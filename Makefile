server = server.py
build_dir = repo

# usage: make preview
preview:
	python $(server)

build:
	python $(server) build
