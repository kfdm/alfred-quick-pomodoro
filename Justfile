_help:
    @just --list

format:
    uvx ruff format
    uvx ruff check --fix

projects:
    uv run timebox-projects

cached:
    uv run timebox-cached

favorites:
    uv run timebox-favorites
