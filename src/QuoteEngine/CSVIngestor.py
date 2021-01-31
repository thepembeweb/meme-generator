"""A CSVIngestor is a csv file processor."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """A CSV file Ingestor class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a CVS file into a list of quotes.

        Args:
            path (str): The path of the CSV file

        Returns:
            list: a list of quotes from the supplied CSV file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest the file')

        quotes = []
        df = pandas.read_csv(path, header=0, delimiter=',')

        for index, row in df.iterrows():
            new_quote = QuoteModel(body=row['body'], author=row['author'])
            quotes.append(new_quote)

        return quotes
