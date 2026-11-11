

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

            partes = url.split("://")
            
            dominio = partes[1].strip().split("/")[0] if len(partes) > 1 else ""
            
            partes_dominio = dominio.split(".")

            if not dominio:
                        print("El dominio está vacío. URL incorrecta.")
                        urls_incorrectas.append(url)
                        continue

            elif len(partes_dominio) >= 2 and all(partes_dominio):
                urls_validas.append(url)
                print("URL válida")

            else:
                urls_incorrectas.append(url)
                print("URL incorrecta")

        case _:
            urls_incorrectas.append(url)
            print("URL incorrecta")


print("\nURLs válidas:")
for url in urls_validas:
    print(url)

print("\nURLs incorrectas:")
for url in urls_incorrectas:
    print(url)