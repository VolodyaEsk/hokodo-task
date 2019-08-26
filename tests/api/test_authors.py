class TestAuthorsApi:

    URL = "/api/authors"

    EXPCTED_DATA = {
        'data':
            {
                'Dr. Jane Doe': ["You Don't Know JS"],
                'Dr. John Doe': ['Understanding ECMAScript 6'],
                'Honoré de Balzac': ['Un début dans la vie', 'Le père Goriot'],
                'Mr. Jane Doe': ['Git Pocket Guide'],
                'Mr. John Doe': ['Programming JavaScript Applications'],
                'Mrs. John Doe': ['Eloquent JavaScript, Second Edition'],
                'Prof. Jane Doe': ['Speaking JavaScript'],
                'Prof. John Doe': ['Learning JavaScript Design Patterns',
                                   'Designing Evolvable Web APIs with ASP.NET']
            }
    }

    def test_get_author_collection(self, client):
        response = client.get(self.URL)
        assert response.status_code == 200
        assert response.json['data'] == self.EXPCTED_DATA['data']


"""
reinstall: clean ## reinstall package
	rm -rf venv/
	make venv

test: venv ## run tests in the tests directory with log level INFO
	pytest --cov=app -s --log-level=INFO tests/

clean: ## clean all useless data
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
"""