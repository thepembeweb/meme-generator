"""A PDFIngestor is a pdf file processor."""
from typing import List
import os
import subprocess
from uuid import uuid4


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """A PDF file Ingestor class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a PDF file into a list of quotes.

        Args:
            path (str): The path of the PDF file

        Returns:
            list: a list of quotes from the supplied PDF file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest the file')

        quotes = []
        tmp_file = f"./tmp/{uuid4()}.txt"
        call = subprocess.call(['pdftotext', path, tmp_file])

        with open(tmp_file, 'r') as infile:
            for line in infile.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(body=parse[0], author=parse[1])
                    quotes.append(new_quote)

        os.remove(tmp_file)
        return quotes
