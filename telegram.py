# ==========================================
# SCRAPER DE TELEGRAM — Paneles solares Cuba
# ==========================================
from telethon.sync import TelegramClient
import pandas as pd
import os
import time

os.makedirs("datos", exist_ok=True)

# ==========================================
# ⚠️ AQUÍ VAN TUS DATOS DE my.telegram.org
# ==========================================
API_ID = 34041342                   
API_HASH = 424b7936895910ebf92b6c5b62184249    
PHONE = "+5351000875              

# ==========================================
# GRUPOS PÚBLICOS CUBANOS DE COMPRAVENTA
# ==========================================
GRUPOS = [
    "compraventacuba",
    "revolico_cuba",
    "ofertascuba",
    "vendocuba",
    "mercaditocuba",
]

# Palabras clave para filtrar anuncios relevantes
PALABRAS = [
    "panel", "solar", "inversor", "bateria", "fotovoltaic",
    "kit solar", "kwh", "vatio", "carga solar"
]

MAX_POR_GRUPO = 100
ARCHIVO = "datos/telegram.csv"

# ==========================================
# SCRAPING
# ==========================================
def scrapear_telegram():
    anuncios = []
    
    with TelegramClient("sesion_cuba", API_ID, API_HASH) as client:
        print("✅ Conectado a Telegram\n")
        
        for grupo in GRUPOS:
            print(f"🔍 Leyendo: {grupo}")
            try:
                count = 0
                for i, msg in enumerate(client.iter_messages(grupo, limit=MAX_POR_GRUPO)):
                    if not msg.text:
                        continue
                    
                    texto_low = msg.text.lower()
                    if any(p in texto_low for p in PALABRAS):
                        anuncios.append({
                            "fuente": f"Telegram:{grupo}",
                            "grupo": grupo,
                            "fecha": msg.date.strftime("%Y-%m-%d %H:%M"),
                            "usuario": str(msg.sender_id) if msg.sender_id else "N/A",
                            "texto": msg.text,
                            "vistas": getattr(msg, "views", 0) or 0,
                            "id_mensaje": msg.id,
                        })
                        count += 1
                
                print(f"   ✅ {count} anuncios relevantes")
                time.sleep(1)
                
            except Exception as e:
                print(f"   ⚠️ No se pudo leer '{grupo}': {e}")
                continue
    
    df = pd.DataFrame(anuncios)
    if len(df) > 0:
        df = df.drop_duplicates(subset=["texto"])
    df.to_csv(ARCHIVO, index=False, encoding="utf-8-sig")
    
    print(f"\n{'='*50}")
    print(f"📁 TOTAL: {len(df)} anuncios guardados en {ARCHIVO}")
    print(f"{'='*50}")
    
    return df

# ==========================================
# EJECUCIÓN
# ==========================================
if name == "__main__":
    df = scrapear_telegram()
    if len(df) > 0:
        print("\n📋 Vista previa:")
        print(df[["grupo", "fecha", "texto", "vistas"]].head(10).to_string())