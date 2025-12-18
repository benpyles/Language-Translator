Translator App
A contemporary, desk-based translation tool using Python and Flet, designed with a dark-themed GUI and supporting real-time translation of languages.
Characteristics

???? Multi-language support English, Spanish, French
• Modern Dark Theme user interface
⚡ Real-time translation service via Google Translation API
•???? Clean UI
???? Language Choice Module
Each

⌨️ Multi-line text input/output support
Screenshots
Show Image
Place your screenshot here

Installing

Prerequisites

For the above code to work properly for

pip (Python package manager)

Setup

.Clone the repository

bashgit clone https://github

cd translator-app
virtual environment creation
bashpython3 -m venv.
source .venv/bin/activate  # On Windows: .ven

Add dependencies
pip install -r requirements.txt
usage
Run your application:

bashpython3 gui

```
1. Choose the source language from "Base Language" drop-down

2. Pick your target language from the "Target Language" dropdown
3. Type your text into the input field
4. Click '文A Translate' to translate
5. Look at translation in output field
## Technology Stack
- *Flet* - UI framework for cross-platform apps
- **deep-translator** - Translation API Wrapper
- **Python 3.12**, Programming Language
# Project Structure
*

translator-app
|
     |
     |
├── gui.py                 # Main application UI

Send request to translation API to translate text.     				├── send_request.py        # Translation API handler
├── hover_animations.py    # UI animations

├──  requirments.txt       # Dependencies for Python
├── README.md          # Project documentation

Dependencies
txtf
deep-trans
Configuration

Currently, the app supports:
English (en)

English (en)

French (fr)
In order to support additional languages, modifications need to be done in the options object of the gui.py file as well as the language codes in the send

Contributing Contributions are always welcome. Please do not hesitate to submit a pull request. Copy the project Create your feature branch (git checkout -b feature/AmazingFeature) Commit changes (git commit -m 'Add some AmazingFeature') Push to branch (git push origin feature/AmazingFeature) Open a Pull Request License This project is licensed under the MIT License. See the LICENSE file for details. ACKNOWLED Flet for the amazing UI framework deep_translator for translation functionalities Contact Your Name - @yourtwitter Project Link: https://github Powered with ❤️ in Flet & Python