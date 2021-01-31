"""A TxtIngestor is a txt file processor."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """A Txt file Ingestor class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a Txt file into a list of quotes.

        Args:
            path (str): The path of the Txt file

        Returns:
            list: a list of quotes from the supplied Txt file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest the file')

        quotes = []

        with open(path, 'r', encoding='utf-8-sig') as infile:
            for line in infile.readlines():
                line = line.strip().split(' - ')
                new_quote = QuoteModel(body=line[0], author=line[1])
                quotes.append(new_quote)

        return quotes
