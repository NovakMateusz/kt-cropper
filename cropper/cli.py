import typer
from pathlib import Path
import logging

from cropper.models import CropManifest, ImageFormat
from cropper.core.processor import handle_request
from cropper.utils.logger import setup_logging

app = typer.Typer(help="Crop images from a PDF using a resource definition.")


@app.command()
def main(
    pdf_path: Path = typer.Argument(..., exists=True, readable=True),
    crop_manifest_path: Path = typer.Option(
        ..., "--crop-manifest-path", exists=True, readable=True
    ),
    output: Path = typer.Option(Path("outputs"), "--output-dir"),
    dpi: int = typer.Option(300, "--dpi"),
    image_format: ImageFormat = typer.Option("PNG", "--image-format"),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable debug logging", is_eager=True
    ),
    log_file: Path | None = typer.Option(None, "--log-file", help="Write logs to a file"),
):
    setup_logging(
        level=logging.DEBUG if verbose else logging.INFO,
        log_file=str(log_file) if log_file else None,
    )

    crop_manifest = CropManifest.model_validate_json(crop_manifest_path.read_text(encoding="UTF-8"))
    output_dir = output / crop_manifest.team_name

    output_dir.mkdir(parents=True, exist_ok=True)

    handle_request(pdf_path, crop_manifest.extractions, dpi, image_format, output_dir)
