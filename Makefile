format:
	pre-commit run --all-files
	python format.py

edit-urls:
	python edit-urls.py

all: format edit-urls
