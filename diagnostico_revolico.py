import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

url = "https://www.revolico.com/search?q=panel-solar"
r = requests.get(url, headers=HEADERS, timeout=15)

print(f"Status: {r.status_code}")
print(f"Tamaño HTML: {len(r.text)} caracteres")
print(f"¿Contiene 'article'?: {'<article' in r.text}")
print(f"¿Contiene 'listing'?: {'listing' in r.text.lower()}")
print(f"¿Contiene 'producto'?: {'producto' in r.text.lower()}")
print(f"¿Contiene 'anuncio'?: {'anuncio' in r.text.lower()}")

# Guardar el HTML para inspeccionar
with open("debug_revolico.html", "w", encoding="utf-8") as f:
    f.write(r.text)
print("\n✅ HTML guardado en debug_revolico.html")

# Mostrar las etiquetas HTML más comunes
soup = BeautifulSoup(r.text, "lxml")
etiquetas = {}
for tag in soup.find_all(True):
    etiquetas[tag.name] = etiquetas.get(tag.name, 0) + 1

print("\n📊 Top 15 etiquetas HTML en la página:")
for nombre, cuenta in sorted(etiquetas.items(), key=lambda x: -x[1])[:15]:
    print(f"   {nombre}: {cuenta}")