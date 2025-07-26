# Markdown to PDF Resume Generator

A modern, minimal CLI tool that converts Markdown-formatted resumes into professional, single-page PDF documents. Built with Python, featuring clean styling and robust error handling.

## ✨ Features

- 🎯 **Single-page validation** - Ensures your resume fits on one page
- 🎨 **Modern, minimal styling** - Professional appearance with clean typography
- 🛡️ **Robust error handling** - Clear error messages for common issues
- 🐳 **Docker support** - Containerized for consistent environments
- 🧪 **Fully tested** - Comprehensive test suite included
- ⚡ **Fast and lightweight** - Minimal dependencies, quick conversion

## 🚀 Quick Start

### Option 1: Local Installation

#### macOS Prerequisites
WeasyPrint requires system libraries that need to be installed first:

```bash
# Install system dependencies with Homebrew
brew install pango gdk-pixbuf libffi cairo
```

#### Setup
```bash
# Clone or download the project
git clone <repository-url>
cd md2pdf-resume-generator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Convert your resume
python main.py sample_resume.md
```

#### Linux Prerequisites
On Ubuntu/Debian systems:
```bash
sudo apt-get install build-essential libpango-1.0-0 libpangocairo-1.0-0 libcairo2 libffi-dev shared-mime-info
```

### Option 2: Docker

```bash
# Build the image
docker build -t md2pdf-resume .

# Convert resume (mount current directory)
docker run --rm -v $(pwd):/app md2pdf-resume sample_resume.md -o resume.pdf
```

## 📖 Usage

### Basic Usage
```bash
# Convert resume.md to resume.pdf
python main.py resume.md

# Specify custom output filename
python main.py resume.md -o my_awesome_resume.pdf

# Use verbose output
python main.py resume.md --verbose
```

### Command Options
```
Arguments:
  input_md          Path to the markdown resume file

Options:
  -o, --output      Output PDF file path (default: input filename with .pdf)
  -t, --template    HTML template path (default: templates/base.html)
  -v, --verbose     Enable verbose output
  --help           Show help message
```

## 📁 Project Structure

```
md2pdf-resume-generator/
├── main.py              # CLI entry point
├── converter.py         # Markdown → HTML → PDF conversion
├── reader.py           # File reading utilities
├── writer.py           # PDF output handling
├── utils.py            # Helper functions
├── exceptions.py       # Custom exception classes
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── templates/
│   └── base.html      # Default HTML template with embedded CSS
├── tests/
│   └── test_converter.py  # Test suite
├── sample_resume.md   # Example resume
└── README.md         # This file
```

## 🎨 Styling

The default template (`templates/base.html`) features:

- **Typography:** Clean, professional fonts (Segoe UI, system fonts)
- **Layout:** Optimized for single-page A4 format
- **Colors:** Minimal color palette with blue accents
- **Spacing:** Carefully tuned margins and line heights
- **Elements:** Styled headings, lists, links, and code blocks

### Customizing Styles

Edit `templates/base.html` to customize:
- Fonts and typography
- Colors and spacing
- Layout and margins
- Page size and orientation

## 📝 Markdown Guidelines

For best results, structure your resume with:

```markdown
# Your Name
**Job Title** | email@example.com | phone | linkedin

---

## Professional Summary
Brief 2-3 sentence summary...

## Technical Skills
- **Category:** Skill list
- **Tools:** Tool list

## Professional Experience
**Job Title** | Company | Dates
- Achievement bullet point
- Another achievement

## Education
**Degree** | University | Year
```

### Single-Page Tips
- Keep content concise and focused
- Use bullet points instead of paragraphs
- Limit work history to most recent/relevant roles
- Use consistent formatting throughout

## 🧪 Testing

### Running Tests

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Run all tests with proper Python path
PYTHONPATH=. pytest tests/ -v

# Run specific test
PYTHONPATH=. pytest tests/test_converter.py::test_markdown_to_html -v
```

### Verification Tests

The project includes comprehensive testing to ensure everything works:

#### 1. Unit Tests
```bash
# All core functionality tests
PYTHONPATH=. pytest tests/ -v
```
Expected output: `6 passed` covering:
- Markdown to HTML conversion
- Template injection
- File reading operations
- PDF generation
- Error handling

#### 2. End-to-End Testing
```bash
# Test basic conversion
python main.py sample_resume.md

# Test with custom output
python main.py sample_resume.md -o custom_resume.pdf

# Test verbose mode
python main.py sample_resume.md --verbose
```

#### 3. Single-Page Validation Test
```bash
# This should fail with page limit error
python main.py long_resume.md
```
Expected output: `❌ Resume exceeds single page limit (generated 3 pages)`

#### 4. CLI Interface Test
```bash
# View help and available options
python main.py --help
```

### Troubleshooting

If you encounter WeasyPrint import errors:

**macOS:**
```bash
# Reinstall system dependencies
brew reinstall pango gdk-pixbuf libffi cairo

# Reinstall Python package
pip uninstall weasyprint
pip install weasyprint
```

**Linux:**
```bash
# Install missing system libraries
sudo apt-get update
sudo apt-get install build-essential libpango-1.0-0 libpangocairo-1.0-0 libcairo2 libffi-dev shared-mime-info
```

## 🐛 Error Handling

The tool provides clear error messages for common issues:

- **File not found:** Missing input files or templates
- **Page limit exceeded:** Content doesn't fit on single page
- **Conversion errors:** Invalid markdown or PDF generation issues
- **Permission errors:** File access or write permission problems

## 🔧 Development

### Setting up for development:

```bash
# Clone repository
git clone <repository-url>
cd md2pdf-resume-generator

# Install system dependencies (macOS)
brew install pango gdk-pixbuf libffi cairo

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run tests to verify setup
PYTHONPATH=. pytest tests/ -v

# Test the application
python main.py sample_resume.md
```

### Dependencies

#### Python Packages
- **markdown:** Markdown to HTML conversion
- **weasyprint:** HTML to PDF rendering
- **typer:** Modern CLI framework
- **pytest:** Testing framework

#### System Dependencies
- **macOS:** `pango`, `gdk-pixbuf`, `libffi`, `cairo` (via Homebrew)
- **Linux:** `libpango-1.0-0`, `libpangocairo-1.0-0`, `libcairo2`, `libffi-dev`, `shared-mime-info`
- **Windows:** WeasyPrint Windows installation guide available [here](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest tests/`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## � Dependencies & Documentation

This project relies on several excellent open-source libraries. Below you'll find links to their official documentation for deeper understanding and advanced usage.

### Core Dependencies

#### [Python Markdown](https://python-markdown.github.io/)
- **Purpose:** Converts Markdown text to HTML
- **Documentation:** https://python-markdown.github.io/
- **API Reference:** https://python-markdown.github.io/reference/
- **Extensions Used:** `extra`, `smarty` for enhanced markdown features
- **GitHub:** https://github.com/Python-Markdown/markdown

#### [WeasyPrint](https://weasyprint.org/)
- **Purpose:** HTML to PDF conversion with CSS support
- **Documentation:** https://doc.courtbouillon.org/weasyprint/stable/
- **Installation Guide:** https://doc.courtbouillon.org/weasyprint/stable/first_steps.html
- **CSS Features:** https://doc.courtbouillon.org/weasyprint/stable/features.html
- **GitHub:** https://github.com/Kozea/WeasyPrint

#### [Typer](https://typer.tiangolo.com/)
- **Purpose:** Modern CLI framework for Python
- **Documentation:** https://typer.tiangolo.com/
- **Tutorial:** https://typer.tiangolo.com/tutorial/
- **API Reference:** https://typer.tiangolo.com/reference/
- **GitHub:** https://github.com/tiangolo/typer

### Development Dependencies

#### [pytest](https://docs.pytest.org/)
- **Purpose:** Testing framework
- **Documentation:** https://docs.pytest.org/en/stable/
- **Getting Started:** https://docs.pytest.org/en/stable/getting-started.html
- **API Reference:** https://docs.pytest.org/en/stable/reference/reference.html
- **GitHub:** https://github.com/pytest-dev/pytest

### System Dependencies

#### WeasyPrint System Requirements
- **macOS:** Requires `pango`, `gdk-pixbuf`, `libffi`, `cairo` via Homebrew
- **Linux:** Requires `libpango-1.0-0`, `libpangocairo-1.0-0`, `libcairo2`, `libffi-dev`, `shared-mime-info`
- **Windows:** See [WeasyPrint Windows Guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)

### Useful Documentation Links

- **Markdown Syntax:** https://daringfireball.net/projects/markdown/syntax
- **CSS for Print Media:** https://developer.mozilla.org/en-US/docs/Web/CSS/@media
- **PDF/A Standards:** https://en.wikipedia.org/wiki/PDF/A
- **Python Packaging:** https://packaging.python.org/en/latest/

## 🙏 Acknowledgments

Special thanks to the maintainers and contributors of the above projects for building such excellent tools that make this project possible.

## 🚀 Future Enhancements

- [ ] Multiple template themes
- [ ] Watch mode for live preview
- [ ] Web interface
- [ ] Export to different page formats
- [ ] Template variable system
- [ ] Dark/light theme variants

---

**Built with much fear and trepidation, hopefully for developers who love Markdown and hand-rolling their own resumes.**
