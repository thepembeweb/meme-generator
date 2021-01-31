"""A MemeEngine is a meme generator."""
from PIL import Image, ImageDraw, ImageFont
import os
from random import randint
from uuid import uuid4


class MemeEngine:
    """A Meme engine class.

    Attributes:
        destination_folder (str): The destination directory path.
    """

    def __init__(self, destination_folder: str):
        """Initialize a new MemeEngine object.

        Args:
            destination_folder (str): The destination directory path

        """
        self.destination_folder = destination_folder

    def draw_caption(self, img: Image, text: str, author: str) -> Image:
        """Draws text and author caption on the supplied image.

        Args:
            img (Image): The supplied image
            text (str): The text of the quote
            author (str): The author of the quote

        Returns:
            Image: an image with a drawn text and author caption if available
        """
        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(
                './fonts/Schoolbell-Regular.ttf',
                size=20)
            draw.text((10, 30), f"{text} - {author}", font=font, fill='white')

        return img

    def resize_image(self, img: Image, width: int) -> Image:
        """Resize the supplied image by the given width.

        Args:
            img (Image): The supplied image
            width (int): The width of the resized image

        Returns:
            Image: an image resized to the given width if available
        """
        if img is not None and width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        return img

    def save_image(self, img: Image) -> str:
        """Save the supplied image.

        Args:
            img (Image): The supplied image

        Returns:
            str: the path of the saved image
        """
        image_path = f"{uuid4()}.png"
        out_path = os.path.join(self.destination_folder, image_path)
        img.save(out_path)

        return out_path

    def make_meme(self, image_path: str, text: str,
                  author: str, width: int = 500) -> str:
        """Create a meme based on supplied image_path, text, author and width.

        Args:
            image_path (Image): The supplied image path
            text (str): The text of the quote
            author (str): The author of the quote
            width (int): The width of the output image
                (default is 500)

        Returns:
            str: the path of the saved image
        """
        img = Image.open(image_path)
        img = self.resize_image(img, width)
        img = self.draw_caption(img, text, author)
        out_path = self.save_image(img)

        return out_path
