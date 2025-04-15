import google.generativeai as genai
from PIL import Image
import requests
import base64
import io

def zrob_plik_txt():
    """Funkcja odpowiada od zapytania uzytkowika o zrobenie pliku txt
    w osobnym pliku jesli chce"""


    if input("czy chesz zapisać odpowiedź w pliku txt? (tak/nie) ") == 'tak'.lower():
        with open('odpowiedzi/odpowiedź.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)



genai.configure(api_key="AIzaSyBxgtw4AMKHevWMv5B0P0A44h4VGJk6DY8")
genai.generation_config = {
    "temperature": 0.4, 
    "top_p": 0.7,
    "top_k": 20,
    "max_output_tokens": 1024,
    "stop_sequences": ["##"],
}

try:
    print("1.Zadać pytanie.")
    print("2.Analiza obrazu")
    print("3.Tłumacz")

    question = int(input("\nWybierz opcje 1-3: "))
    if question == 1:

        model = genai.GenerativeModel('models/gemini-1.5-flash')

        if input("Chcesz sam nadać rolę ai? (tak/nie) ") == 'tak'.lower():
            role_prompt = input("Nadaj rolę: ")
        else:
            role_prompt = "Jesteś profesjonalistą w wiedzy ogólnej i masz bardzo dokładne i precyzyjne odpowiedzi"

        message = input("Zadaj pytanie: ")
        response = model.generate_content(f"{role_prompt}\n{message}")
        
        zrob_plik_txt()

        print("\nOdpowiedz:")
        print(response.text)

    elif question == 2:

        model = genai.GenerativeModel('models/gemini-1.5-flash')
        image_path = input("Podaj ścieżkę do obrazu: ")
        image = Image.open(image_path)
        message = input("Zadaj pytanie o obraz: ")
        response = model.generate_content([message, image])

        zrob_plik_txt()

        print("\nOdpowiedź:")
        print(response.text)

    elif question == 3:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        role_prompt = """Jesteś tłumaczem klasy światowej. Twoje zadania to:
1. Wykrywanie języka podanego tekstu
2. Tłumaczenie tekstu na język polski
3. Ignorowanie wszystkich pytań niezwiązanych z tłumaczeniem
4. Odpowiadanie tylko w kontekście tłumaczenia
5. Gdy ktoś napisze coś po polsku, odpowiedz ze tekst jest juz przetlumaczony

Przetłumacz następujący tekst:"""

        message = input("Napisz teskt jaki chce aby ci przetłumaczył: ")
        response = model.generate_content(f"{role_prompt}\n{message}")

        zrob_plik_txt()
        print("Odpowwiedz: \n")
        print(response.text)

except Exception as e:
    print(f"\nWystąpił błąd: {e}")
