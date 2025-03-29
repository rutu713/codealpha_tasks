from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# User Input
text = input("Enter text to translate: ")
target_language = input("Enter target language code (e.g., fr, es, hi): ")
translated_text = translate_text(text, target_language)

print("Translated Text:", translated_text)
