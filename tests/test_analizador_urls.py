urls_validas = []
urls_incorrectas = []

while True:

    url = input("Introduce una URL: ").strip()

    if not url:
        print("La entrada está vacía. Por favor, introduce una URL válida.")
        continue

    elif url.lower() == "fin":
        break

    match url:
        case url if url.startswith(("https://", "http://")):
            urls_validas.append(url)
            print("URL válida")

        case _:
            urls_incorrectas.append(url)
            print("URL incorrecta")


print("\nURLs válidas:")
for url in urls_validas:
    print(url)

print("\nURLs incorrectas:")
for url in urls_incorrectas:
    print(url)

'''

siguiente paso será comprobar que después de https:// o http:// exista un dominio.

 utilizar .split().

antes de Selenium.'''