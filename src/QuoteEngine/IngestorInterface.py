"""An Ingestor interface module."""
from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Ingestor base abstract class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions.
    """

    allowed_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether file extension is supported by the ingestors.

        Args:
            path (str): The path of the file

        Returns:
            bool: True if successful, False otherwise.
        """
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file into a list of quotes.

        Args:
            path (str): The path of the file

        Returns:
            list: a list of quotes from the supplied file
        """
        pass
