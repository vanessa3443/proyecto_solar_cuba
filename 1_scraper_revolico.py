# ==========================================
# SCRAPER DE REVOLICO — Paneles solares Cuba
# ==========================================
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
import time

# Crear carpeta datos si no existe
os.makedirs("datos", exist_ok=True)

# ==========================================
# CONFIGURACIÓN
# ==========================================
BUSQUEDAS = [
    "panel-solar",
    "paneles-solares",
    "kit-solar",
    "inversor-solar",
    "bateria-litio",
    "energia-solar",
]

ARCHIVO = "datos/revolico.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

# ==========================================
# FUNCIÓN DE SCRAPING
# ==========================================
def scrapear_revolico():
    anuncios = []
    
    for termino in BUSQUEDAS:
        url = f"https://www.revolico.com/search?q={termino}"
        print(f"\n🔍 Buscando: {termino}")
        print(f"   URL: {url}")
        
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            print(f"   Status: {r.status_code}")
            
            if r.status_code != 200:
                print("   ⚠️ No se pudo acceder")
                continue
            
            soup = BeautifulSoup(r.text, "lxml")
            tarjetas = soup.find_all("article")
            print(f"   Tarjetas encontradas: {len(tarjetas)}")
            
            for tarjeta in tarjetas:
                try:
                    titulo_tag = tarjeta.find(["h2", "h3", "a"])
                    titulo = titulo_tag.get_text(strip=True) if titulo_tag else ""
                    
                    precio_tag = tarjeta.find(string=re.compile(r"\$|USD|CUP|MLC"))
                    precio = precio_tag.strip() if precio_tag else ""
                    
                    enlace_tag = tarjeta.find("a", href=True)
                    enlace = enlace_tag["href"] if enlace_tag else ""
                    if enlace and not enlace.startswith("http"):
                        enlace = "https://www.revolico.com" + enlace
                    
                    if titulo:
                        anuncios.append({
                            "fuente": "Revolico",
                            "termino": termino,
                            "titulo": titulo,
                            "precio_texto": precio,
                            "url": enlace,
                            "fecha": time.strftime("%Y-%m-%d %H:%M")
                        })
                except Exception:
                    continue
            
            time.sleep(2)
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue
    
    df = pd.DataFrame(anuncios)
    df = df.drop_duplicates(subset=["titulo"])
    df.to_csv(ARCHIVO, index=False, encoding="utf-8-sig")
    
    print(f"\n{'='*50}")
    print(f"📁 TOTAL: {len(df)} anuncios guardados en {ARCHIVO}")
    print(f"{'='*50}")
    
    return df

# ==========================================
# EJECUCIÓN
# ==========================================
if __name__=="__main__":
    df = scrapear_revolico()
    if len(df) > 0:
        print("\n📋 Vista previa:")
        print(df[["titulo", "precio_texto", "url"]].head(10).to_string())