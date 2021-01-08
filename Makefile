PIP_BIN := .venv/bin/pip

.PHONY:	pip
pip: ${PIP_BIN}
	${PIP_BIN} install -e .

$(PIP_BIN):
	python3 -m venv .venv

.PHONY: projects
projects: ${PIP_BIN}
	.venv/bin/timebox-projects

.PHONY: cached
cached: ${PIP_BIN}
	.venv/bin/timebox-cached

.PHONY: favorites
favorites: ${PIP_BIN}
	.venv/bin/timebox-favorites


clean:
	rm -rf .venv
