import typer
from pathlib import Path
import logging

from cropper.models import Resources, ImageFormat
from cropper.core.processor import handle_request
from cropper.utils.logger import setup_logging

app = typer.Typer(help="Crop images from a PDF using a resource definition.")


@app.command()
def main(
    pdf_path: Path = typer.Argument(..., exists=True, readable=True),
    resource_path: Path = typer.Option(..., "--resource-path", exists=True, readable=True),
    output_dir: Path = typer.Option(Path("outputs"), "--output-dir"),
    dpi: int = typer.Option(300, "--dpi"),
    image_format: ImageFormat = typer.Option("PNG", "--image-format"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable debug logging", is_eager=True),
    log_file: Path | None = typer.Option(None, "--log-file", help="Write logs to a file"),
):
    setup_logging(
        level=logging.DEBUG if verbose else logging.INFO,
        log_file=str(log_file) if log_file else None,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    resources = Resources.validate_json(resource_path.read_text(encoding="UTF-8"))
    handle_request(pdf_path, resources, dpi, image_format, output_dir)
