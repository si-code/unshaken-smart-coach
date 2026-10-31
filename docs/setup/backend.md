
# Backend setup

The backend uses Python, FastAPI, and uv. uv manages the project's
Python version, virtual environment, dependencies, and locked dependency
versions, so contributors do not need to manage a project environment with
`pip` and `venv` separately.

> **Current status:** The initial backend application has been scaffolded.
> The FastAPI application and basic endpoint tests have been created.
> Database migration configuration has not yet been implemented.

## Prerequisites

- Git and a local clone of this repository.
- Docker with Docker Compose.
- The local PostgreSQL service described in [postgresql.md](postgresql.md).
- uv.

The current local backend configuration uses Python 3.13.
The supported project-wide Python version should be confirmed with the team.

## Install uv

Choose one installation method.

### Windows

Using WinGet:

```powershell
winget install --id=astral-sh.uv -e
```

Or use uv's official installer:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS and Linux

Using uv's official installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Homebrew users may instead run:

```bash
brew install uv
```

Open a new terminal and verify the installation:

```text
uv --version
```

Review downloaded installation scripts before running them if required by your
organization's security policy. See the [official uv installation guide][uv-install]
for other supported installation methods.

## Backend commands

Run these commands from the repository root unless otherwise specified.

Install the declared Python version and synchronize dependencies:

```bash
cd backend
uv sync
```

Run the development API:

```bash
uv run fastapi dev app/main.py
```

Run backend tests:

```bash
uv run pytest
```

The initial application provides:

- `GET /` — API welcome message.
- `GET /health` — basic health status.

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

Database migrations are not available yet. The command
`uv run alembic upgrade head` should be used after migration configuration
and approved migrations have been implemented.

## Dependency rules

- Add runtime dependencies with `uv add <package>`.
- Add development dependencies with `uv add --dev <package>`.
- Commit both `pyproject.toml` and `uv.lock`.
- Do not commit `.venv/`; it is machine-specific and ignored by Git.
- Run project commands through `uv run` so they use the managed environment.
- Do not place database passwords, AWS credentials, or API keys in source code.

[uv-install]: https://docs.astral.sh/uv/getting-started/installation/
