import google.generativeai as genai
from PIL import Image
import requests
import base64
import io

# Konfiguracja API
genai.configure(api_key="AIzaSyBxgtw4AMKHevWMv5B0P0A44h4VGJk6DY8")
\
# Użyjmy dostępnego modelu
try:
    print("1.Zadać pytanie.")
    print("2.Analiza obrazu")
    print("3.Tłumacz")

    question = int(input("\nWybierz opcje 1-3: "))
    if question == 1:

        model = genai.GenerativeModel('models/gemini-1.5-flash')
        message = input("Zadaj pytanie: ")
        response = model.generate_content(message)

        if input("czy chesz zapisać odpowiedź w pliku txt? (tak/nie) ") == 'tak':
            with open('odpowiedzi/odpowiedź.txt', 'w', encoding='utf-8') as file:
                file.write(response.text)

        print("\nOdpowiedz:")
        print(response.text)

    elif question == 2:

        model = genai.GenerativeModel('models/gemini-1.5-flash')
        image_path = input("Podaj ścieżkę do obrazu: ")
        image = Image.open(image_path)
        message = input("Zadaj pytanie o obraz: ")
        response = model.generate_content([message, image])

        if input("czy chesz zapisać odpowiedź w pliku txt? (tak/nie) ") == 'tak':
            with open('odpowiedź.txt', 'w', encoding='utf-8') as file:
                file.write(response.text)

        print("\nOdpowiedź:")
        print(response.text)

    elif question == 3:

        model = genai.GenerativeModel('models/gemini-1.5-flash')
        message = input("Napisz teskt jaki chce aby ci przetłumaczył: ")
        
except Exception as e:
    print(f"\nWystąpił błąd: {e}")
