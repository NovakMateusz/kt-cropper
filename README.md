# KillTeam Cropper

A holy Python CLI relic blessed by the Omnissiah. This tool chants binary litanies at Games Workshop PDFs and, guided by ancient configuration scrolls, surgically extracts individual datacards from the blessed tomes. Each card is purified, cropped, and sealed into its own sacred file—ready for battle, printing, or ritual consultation mid-skirmish. No daemons were summoned (probably), but many PDFs were appeased. Glory to the Machine God, and may your datacards always be perfectly aligned.

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
git clone https://github.com/NovakMateusz/kt-cropper.git
cd kt-cropper
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
When activating a Python virtual environment on Windwos, PowerShell may display an error stating that script execution is disabled on current system. This happens because the virtual environment activation script (**Activate.ps1**) is considered an unsigned script and is therefore blocked by the current execution policy. Running:
```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```
temporarily relaxes the execution policy **only for the current PowerShell session**, allowing scripts (such as virtual environment activation scripts) to run. It does not change system-wide or user-level security settings and is reset when the session is closed.

### Install the tool (editable mode)
```bash
uv pip install -e .
```

This will:
- Install dependencies
- Register the cropper CLI command
- Keep the code editable for development

## Usage
```bash
kt_cropper [OPTIONS] PDF_PATH
```

### Arguments
PDF_PATH (required)  
Path to the input PDF file containing the datacards to be extracted.

### Options
-m, --crop-manifest-path (required)  
Path to the crop manifest file. The manifest defines how and where datacards should be detected and cropped from the PDF.

-o, --output-dir  
Directory where extracted datacards will be saved.  
Default: outputs

-d, --dpi  
DPI (dots per inch) used when rendering the PDF pages to images before cropping. Higher values result in better image quality at the cost of increased processing time and file size.
Default: 300

-f, --image-format  
Output image format for the extracted datacards.  
Default: PNG

-v, --verbose  
Enable verbose (debug-level) logging. Useful for troubleshooting crop issues or manifest errors.

--log-file  
Write logs to a specified file instead of (or in addition to) standard output.

## Examples
see the [examples](examples/README.md)
