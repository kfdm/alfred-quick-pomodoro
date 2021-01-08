PIP_BIN := .venv/bin/pip

.PHONY:	pip
pip: ${PIP_BIN}
	${PIP_BIN} install -e .

$(PIP_BIN):
	python3 -m venv .venv

clean:
	rm -rf .venv
