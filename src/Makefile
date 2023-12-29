PYTHON=python3

all: clean venv install_core install_app

venv:
	$(PYTHON) -m venv venv
	source venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

install_core:
	cd model/core && $(PYTHON) setup.py build_ext -i

install_app:
	$(PYTHON) setup.py py2app -A
	productbuild --component dist/SmartCalc_v3.app dist/SmartCalc_v3.pkg

tests: install_core
	$(PYTHON) test.py -v

clean:
	rm -rf __pycache__ build dist venv history.txt
	rm -rf view/__pycache__
	rm -rf presenter/__pycache__
	rm -rf model/__pycache__
	rm -rf .pytest_cache
	rm -rf model/core/build
	rm -rf model/core/*.so