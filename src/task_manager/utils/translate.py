from googletrans import Translator

def translate_text(text, dest_language):
    lang_codes = {
        "english": "en",
        "portuguese": "pt",
        "spanish": "es",
        "french": "fr",
        # Add other languages as necessary
    }
    dest_language_code = lang_codes.get(dest_language.lower(), "en")
    translator = Translator()

    if isinstance(text, list):
        translated_list = [translator.translate(item, dest=dest_language_code).text for item in text]
        return translated_list
    else:
        translated = translator.translate(text, dest=dest_language_code).text
        return translated
