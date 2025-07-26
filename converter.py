import markdown
import weasyprint
import io
from exceptions import ConversionError, PageLimitError


def markdown_to_html(md_text: str) -> str:
    """Convert markdown text to HTML."""
    return markdown.markdown(md_text, extensions=["extra", "smarty"])


def html_to_pdf(html: str, output_path: str) -> None:
    """Convert HTML to PDF with single-page validation."""
    try:
        # Create WeasyPrint HTML document
        html_doc = weasyprint.HTML(string=html)

        # Generate PDF in memory first to check page count
        pdf_bytes = io.BytesIO()
        document = html_doc.render()

        # Check page count
        page_count = len(document.pages)
        if page_count > 1:
            raise PageLimitError(f"Resume exceeds single page limit (generated {page_count} pages). " f"Please reduce content or adjust formatting.")

        # If single page, write to file
        html_doc.write_pdf(output_path)

    except PageLimitError:
        raise  # Re-raise page limit errors
    except Exception as e:
        raise ConversionError(f"Failed to convert HTML to PDF: {e}")
