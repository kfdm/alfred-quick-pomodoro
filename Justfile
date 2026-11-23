_help:
    @just --list

format:
    just --fmt
    uvx ruff format
    uvx ruff check --fix

projects *args:
    uv run timebox-projects {{ args }}

cached *args:
    uv run timebox-cached {{ args }}

favorites *args:
    uv run timebox-favorites {{ args }}

start *args:
    uv run timebox-start  {{ args }}
