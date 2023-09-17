# Python Translation App "Language Exchange"

A simple translation app created with Python, featuring a basic graphical user interface (GUI). This app allows users to translate text from one language to another quickly and easily.

## Features

- Translate text between multiple languages.
- Choose the source and target languages from dropdown menus.
- Clear the input and output text fields.
- Easy-to-use graphical interface.

## Usage

1. Enter the text you want to translate in the "Enter text" field.
2. Select the source language from the "Choose input language" dropdown.
3. Select the target language from the "Choose output language" dropdown.
4. Click the "Translate" button to translate the text.
5. The translated text will appear in the "Output" field.
6. To clear the text fields, click the "Clear" button.

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/yourrepository.git
2. Navigate to the project directory:
   cd Python-Translator
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the application:
   python main.py

## Libraries and APIs Used

- `ssl`: Used for handling SSL/TLS connections with `_create_unverified_context`.
- `tkinter`: Used for creating the GUI.
- `libretranslatepy`: A Python wrapper for the LibreTranslate API, which provides language detection and translation services.

## License

This project is licensed under the MIT License
