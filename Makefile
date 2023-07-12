# Start the unittestsS
test:
	python3 -m unittest tests/test_enter_names.py

python-package-install:
	try:
		if ! which poetry; then echo "Poetry not found - installing via pip"; python3 -m pip install poetry ; fi
	exept:
		if ! which poetry; then echo "pip not found - installing via apt"; sudo apt install -y python3-poetry; fi
	poetry install