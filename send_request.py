from deep_translator import GoogleTranslator
import time

LANGUAGES = ['fr', 'it', 'es', 'ru', 'en', 'zh-Hant']

#Defines function to send requests to translator server
def send_request(message, lang_to, lang_from):
    translator = GoogleTranslator(source=lang_from, target=lang_to)
    translation = translator.translate(str(message))
    return translation