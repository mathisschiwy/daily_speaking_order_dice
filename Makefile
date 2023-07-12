# Start the unittestsS
test:
	python3 -m unittest tests/test_enter_names.py

python-package-install:
	if ! which poetry; then echo "Poetry not found - installing"; python3 -m pip install poetry ; fi
	poetry install