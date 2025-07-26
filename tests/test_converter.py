import pytest
import os
import tempfile
from converter import markdown_to_html, html_to_pdf
from reader import read_markdown, read_template
from utils import inject_html_into_template
from exceptions import ResumeGenError


def test_markdown_to_html():
    """Test markdown to HTML conversion."""
    md = "# John Doe\n\nSoftware Engineer with *5 years* experience."
    html = markdown_to_html(md)
    assert "<h1>John Doe</h1>" in html
    assert "<em>5 years</em>" in html


def test_template_injection():
    """Test HTML content injection into template."""
    template = "<html><body>{{ content }}</body></html>"
    content = "<h1>Test</h1>"
    result = inject_html_into_template(template, content)
    assert result == "<html><body><h1>Test</h1></body></html>"


def test_read_markdown_file():
    """Test reading markdown from file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("# Test Resume\n\nContent here.")
        temp_path = f.name

    try:
        content = read_markdown(temp_path)
        assert "# Test Resume" in content
        assert "Content here." in content
    finally:
        os.unlink(temp_path)


def test_read_template_file():
    """Test reading template from file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as f:
        f.write("<html>{{ content }}</html>")
        temp_path = f.name

    try:
        content = read_template(temp_path)
        assert "{{ content }}" in content
    finally:
        os.unlink(temp_path)


def test_html_to_pdf_single_page():
    """Test HTML to PDF conversion with single page content."""
    html = """
    <html>
    <head><style>body { font-size: 12pt; }</style></head>
    <body>
        <h1>Short Resume</h1>
        <p>Brief content that fits on one page.</p>
    </body>
    </html>
    """

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        temp_path = f.name

    try:
        html_to_pdf(html, temp_path)
        assert os.path.exists(temp_path)
        assert os.path.getsize(temp_path) > 0
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_file_not_found_error():
    """Test error handling for missing files."""
    with pytest.raises(ResumeGenError):
        read_markdown("nonexistent.md")

    with pytest.raises(ResumeGenError):
        read_template("nonexistent.html")
