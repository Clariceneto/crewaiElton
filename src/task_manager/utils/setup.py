import os
from dotenv import load_dotenv
from translate import Translator

def setup_environment():
    load_dotenv()
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation
