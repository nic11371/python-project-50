class FormatError(Exception):
    """Exception raised for custom format in the application."""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{self.message}"
