from deep_translator import GoogleTranslator
import time

LANGUAGES = ['fr', 'it', 'es', 'ru', 'en', 'zh-Hant']

def send_request(message, lang):
    for language in LANGUAGES:
        try:
            translator = GoogleTranslator(source=lang, target=language)
            translation = translator.translate(str(message))
            print(f'{language}: {translation}')
            time.sleep(0.5)  # Small delay to be respectful to the API
        except Exception as e:
            print(f'{language}: Error - {e}')