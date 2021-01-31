"""A DocxIngestor is a docx file processor."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """A Docx file Ingestor class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions.
    """

    allowed_extensions = ['doc', 'docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a Docx file into a list of quotes.

        Args:
            path (str): The path of the Docx file

        Returns:
            list: a list of quotes from the supplied Docx file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest the file')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(body=parse[0], author=parse[1])
                quotes.append(new_quote)

        return quotes
