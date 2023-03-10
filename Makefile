#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python -m pip install -e .[develop]

build:  ## build the python library
	python setup.py build build_ext --inplace

install:  ## install library
	python -m pip install .

#########
# LINTS #
#########
lint:  ## run static analysis with flake8
	python -m black --check splitinerary setup.py
	python -m flake8 splitinerary setup.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black splitinerary/ setup.py

# alias
fix: format

#########
# TESTS #
#########
test: ## clean and run unit tests
	python -m unittest discover test/ "test_*.py"

coverage:  ## clean and run unit tests with coverage
	coverage run -m unittest discover test/ "test_*.py"
	coverage report
	coverage html

# Alias
tests: test


#########
# CLEAN #
#########
deep-clean: ## clean everything from the repository
	git clean -fdx

clean: ## clean the repository
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info .pytest_cache

############################################################################################

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: develop build install lint lints format fix check checks annotate test coverage show-coverage tests show-version patch minor major dist-build dist-check dist publish deep-clean clean help