import typer
import sys
import os
from pathlib import Path
from reader import read_markdown, read_template
from converter import markdown_to_html, html_to_pdf
from writer import write_pdf
from utils import inject_html_into_template, setup_logging
from exceptions import ResumeGenError

app = typer.Typer(help="Convert Markdown resumes to professional PDF documents.")


def get_output_path(input_path: str, output_path: str = None) -> str:
    """Generate output path if not provided."""
    if output_path:
        return output_path

    # Convert input.md to input.pdf
    input_stem = Path(input_path).stem
    return f"{input_stem}.pdf"


@app.command()
def main(
    input_md: str = typer.Argument(..., help="Path to the markdown resume file"),
    output: str = typer.Option(None, "--output", "-o", help="Output PDF file path"),
    template: str = typer.Option("templates/base.html", "--template", "-t", help="HTML template path"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
):
    """
    Convert a Markdown resume to a professional PDF.

    Examples:
        python main.py resume.md
        python main.py resume.md -o my_resume.pdf
        python main.py resume.md --template custom.html
    """
    if verbose:
        setup_logging()

    output_path = get_output_path(input_md, output)

    try:
        # Validate input file exists
        if not os.path.exists(input_md):
            typer.echo(f"❌ Input file not found: {input_md}", err=True)
            sys.exit(1)

        if verbose:
            typer.echo(f"📄 Reading markdown from: {input_md}")

        # Read and process files
        markdown_content = read_markdown(input_md)
        html_body = markdown_to_html(markdown_content)

        if verbose:
            typer.echo(f"🎨 Using template: {template}")

        template_html = read_template(template)
        full_html = inject_html_into_template(template_html, html_body)

        if verbose:
            typer.echo(f"🔄 Converting to PDF...")

        # Convert to PDF with single-page validation
        html_to_pdf(full_html, output_path)

        # Verify output
        if write_pdf(output_path):
            typer.echo(f"✅ Resume successfully generated: {output_path}")
            if verbose:
                file_size = os.path.getsize(output_path)
                typer.echo(f"📊 File size: {file_size:,} bytes")
        else:
            typer.echo(f"❌ Failed to write PDF file: {output_path}", err=True)
            sys.exit(1)

    except ResumeGenError as e:
        typer.echo(f"❌ {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"❌ Unexpected error: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    app()
