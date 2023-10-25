import requests

def get_webpage_content(url):
    try:
        response = requests.get(url)
        # Verifica che la richiesta HTTP sia stata eseguita con successo
        if response.status_code == 200:
            return response.text  # Restituisce il contenuto HTML della pagina
        else:
            return f"Errore nella richiesta HTTP. Codice di stato: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Errore nella richiesta HTTP: {str(e)}"

if __name__ == '__main__':
    url = input("Inserisci l'URL della pagina web: ")
    content = get_webpage_content(url)

    if content:
        print("Contenuto della pagina web:")
        print(content)
    else:
        print("Impossibile ottenere il contenuto della pagina.")
