"""An Ingestor is a file processor."""
from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor

from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """A file ingestor class.

    Attributes:
        ingestors (list): A list of file ingestors.
    """

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file.

        Args:
            path (str): The path of the file

        Returns:
            list: a list of quotes from the supplied file

        Raises:
            Exception: An ingestor could not be found for the supplied file.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception('Ingestor not found for the supplied file')
