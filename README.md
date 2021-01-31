# Dog Meme Generator

> This project showcases a multimedia application to dynamically generate memes, including an image with an overlaid quote. It is built as a Flask app that uses a Quote Engine Module and Meme Generator Modules to generate a random captioned image.

![](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)


## Dog meme generator demo

![](meme-demo.gif)


## Overview

The application showaces the following features:

* Interaction with a variety of complex filetypes.
* Loading quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
* Loading, manipulating, and saving images.
* Accepting dynamic user input through a command-line tool and a web service.
* Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
* DRY (don't repeat yourself) principles of class and method design.
* Working with modules and packages in Python.
* Coding best practices for style and documentation
* Ensuring that code, docstrings, and comments adhere to [PEP 8 Standards](https://www.python.org/dev/peps/pep-0008/).


## Quote Engine

The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:
```bash
"This is a quote body" - Author
```

The module is composed of the following classes:

* **QuoteModel** - An class to encapsulate the body and author
* **IngestorInterface** - An abstract base class for Ingestors that defines two methods with the following class method signatures:
  ```bash
  def can_ingest(cls, path: str) -> boolean
  def parse(cls, path: str) -> List[QuoteModel]
  ```
* **Ingestor** - A class that realizes the IngestorInterface and encapsulates the helper classes
* **CSVIngestor** - A helper class that implements a strategy object that realizes the `IngestorInterface` for a csv file type
* **DocxIngestor** - A helper class that implements a strategy object that realizes the `IngestorInterface` for a docx file type
* **PDFIngestor** - A helper class that implements a strategy object that realizes the `IngestorInterface` for a pdf file type
* **TxtIngestor** - A helper class that implements a strategy object that realizes the `IngestorInterface` for a txt file type


## Meme Engine

The Meme Engine Module is responsible for manipulating and drawing text onto images

This module is composed of the following classes:

* **MemeEngine** - A Meme Generator class that implements the following instance method signature, which returns the path to the manipulated image:
  ```bash
  make_meme(self, img_path, text, author, width = 500) -> str
  ```


## Installation

### Requirements
The project requires `pip` installed.

If you do not have `pip` installed, you can download it here: [pip](https://pip.pypa.io/en/stable/installing/)

### Setup

Clone the source locally:

```sh
$ git clone https://github.com/thepembeweb/meme-generator.git
$ cd meme-generator
```

Install project dependencies:

```sh
$ pip install -r requirements.txt
```

### Running the CLI application

Generate meme with defined arguments

```sh
$ cd src
$ python3 meme.py \
  --path './_data/photos/dog/xander_2.jpg' \
  --body 'I'm a happy dog' \
  --author 'Rex'
```

Generate meme with no defined arguments

```sh
$ cd src
$ python3 meme.py
```

### Running the Web application

Start the development server:

```sh
$ cd src
$ python app.py
```

Open the browser at `localhost:5000`


## Built With

* [Python 3](https://www.python.org/) - The programming language used
* [Flask](https://palletsprojects.com/p/flask/) - The web framework used


## Authors

* **[Pemberai Sweto](https://github.com/thepembeweb)** - *Initial work* - [Dog Meme Generator](https://github.com/thepembeweb/meme-generator)

## License

[![License](http://img.shields.io/:license-mit-green.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
- Copyright 2021 © [Pemberai Sweto](https://github.com/thepembeweb).
