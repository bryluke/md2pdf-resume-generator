class ResumeGenError(Exception):
    """Base exception for resume generation errors."""
    pass


class FileNotFoundError(ResumeGenError):
    """Raised when input files cannot be found."""
    pass


class ConversionError(ResumeGenError):
    """Raised when HTML to PDF conversion fails."""
    pass


class PageLimitError(ResumeGenError):
    """Raised when resume exceeds single page limit."""
    pass
