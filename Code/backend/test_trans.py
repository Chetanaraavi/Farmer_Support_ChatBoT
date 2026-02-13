import sys
import io

# Force UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from googletrans import Translator

def test_translation():
    translator = Translator()
    text = "How can I apply for the Pradhan Mantri Fasal Bima Yojana?"
    try:
        # Test translation to Hindi
        translated = translator.translate(text, dest='hi')
        print(f"Original: {text}")
        print(f"Translated (Hindi): {translated.text}")
        
        # Test translation back to English (simulating user input)
        telugu_text = "ప్రధాన్ మంత్రి ఫసల్ బీమా యోజన కోసం నేను ఎలా దరఖాస్తు చేసుకోవాలి?" # Telugu
        translated_back = translator.translate(telugu_text, src='te', dest='en')
        print(f"Original (Telugu): {telugu_text}")
        print(f"Translated (English): {translated_back.text}")
        
    except Exception as e:
        print(f"Translation failed: {e}")

if __name__ == "__main__":
    test_translation()
