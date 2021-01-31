"""Quote model module."""


class QuoteModel:
    """Simple POPO Object to represent a Quote."""
    def __init__(self, body: str, author: str):
        """Initialize a new QuoteModel object.

        Args:
            body (str): The body of the quote
            author (str): The author of the quote
        """
        self.author = author
        self.body = body

    def __repr__(self):
        """Get string representation of QuoteModel object."""
        return f"{self.body} by {self.author}"
