import random
import os
import requests
import uuid
from flask import Flask, render_template, abort, request

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    # imgs = [images_path + i for i in os.listdir(images_path)]
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    r = requests.get(image_url)

    image_file_name = f'./static/{uuid.uuid4()}.png'

    with open(image_file_name, 'wb') as outfile:
        outfile.write(r.content)

    body = request.form.get('body')
    author = request.form.get('author')
    path = meme.make_meme(image_file_name, body, author)
    os.remove(image_file_name)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
