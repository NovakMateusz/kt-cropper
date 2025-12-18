# KillTeam Cropper

## Requirements
- git
- Python 3.13+
- uv (Python package & environment manager)

## Installing uv

### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Restart your terminal after installation.

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installation

### Clone the repository
```bash
git clone https://github.com/your-org/cropper.git
cd cropper
```

### Create a virtual environment
```bash
uv venv
```
This creates a .venv/ directory in the project root.

### Activate virtual environment

macOS / Linux
```bash
source .venv/bin/activate
```

Windows
```powershell
.\.venv\Scripts\activate
```

### Install the tool (editable mode)
```bash
uv pip install -e .
```

This will:
- Install dependencies
- Register the cropper CLI command
- Keep the code editable for development

## Usage


