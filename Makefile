format:
	pre-commit run --all-files
	python format.py

metadata:
	python metadata.py

edit-urls:
	python edit-urls.py

all: format metadata edit-urls
