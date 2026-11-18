from urllib.parse import urlsplit


def es_url_valida(url: str) -> bool:
    try:
        parsed = urlsplit(url.strip())
        dominio = parsed.hostname

        return (
            parsed.scheme in {"http", "https"}
            and bool(dominio)
            and len(dominio.split(".")) >= 2
            and all(dominio.split("."))
        )
    except ValueError:
        return False


def main() -> None:
    urls_validas = []
    urls_incorrectas = []

    while True:
        url = input("Introduce una URL: ").strip()

        if not url:
            print("La entrada está vacía. Por favor, introduce una URL válida.")
            continue

        if url.lower() == "fin":
            break

        if es_url_valida(url):
            urls_validas.append(url)
            print("URL válida")
        else:
            urls_incorrectas.append(url)
            print("URL incorrecta")

    print("\nURLs válidas:")
    for url in urls_validas:
        print(url)

    print("\nURLs incorrectas:")
    for url in urls_incorrectas:
        print(url)


if __name__ == "__main__":
    main()
