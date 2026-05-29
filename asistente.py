import json

def cargar_conocimiento():
    with open('datos_salta.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def mostrar_recomendacion(destino):
    print(f"\n🌟 Recomendación: {destino['nombre']}")
    print(f"📝 {destino['descripcion']}")
    print(f"🔗 Más información: {destino['url']}")

def iniciar_asistente():
    datos = cargar_conocimiento()
    
    print("==================================================")
    print("🏔️ ¡Hola! Soy tu IA de Turismo y Eventos en Salta.")
    print("==================================================")
    
    primer_destino = datos['destinos'][0]
    mostrar_recomendacion(primer_destino)

if __name__ == "__main__":
    iniciar_asistente()