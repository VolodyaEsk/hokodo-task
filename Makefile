# Some simple testing tasks (sorry, UNIX only).


venv install:  ## create virtualenv if not exists and install package
	test -d venv || virtualenv venv --python=$$(which python3); . venv/bin/activate; pip install -r requirements.txt

reinstall: clean  ## reinstall package
	rm -rf venv/
	make venv

run: venv  ## run flask application
	. venv/bin/activate; flask run

test coverage: venv  ## run tests in the tests directory with log level INFO and get covarage info
	. venv/bin/activate; pytest --cov=app -s --log-level=INFO tests

clean:  ## clean all useless data
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage

help:  ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
