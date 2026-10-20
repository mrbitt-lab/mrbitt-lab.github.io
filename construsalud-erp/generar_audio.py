# Genera la voz del video con una voz neural en español (igual en todos los navegadores).
# Uso, desde la carpeta que contiene index.html y narr.json:
#   pip install edge-tts
#   python3 generar_audio.py
# Crea audio/<escena>-<frase>.mp3. El video los usa solos; si faltan, usa la voz del navegador.
import asyncio, json, pathlib
import edge_tts

VOZ = "es-MX-DaliaNeural"   # alternativas: es-MX-JorgeNeural, es-CO-SalomeNeural, es-VE-PaolaNeural
narr = json.load(open("narr.json", encoding="utf-8"))
out = pathlib.Path("audio"); out.mkdir(exist_ok=True)

async def main():
    for i, frases in enumerate(narr, 1):
        for k, t in enumerate(frases):
            await edge_tts.Communicate(t, VOZ, rate="+0%").save(str(out / f"{i}-{k}.mp3"))
            print("ok", i, k)
asyncio.run(main())
