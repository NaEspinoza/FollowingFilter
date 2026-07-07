import json
import argparse
import sys

def cargar_usuarios_seguidores(ruta_followers):
    try:
        with open(ruta_followers, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Instagram a veces envuelve la lista directamente o dentro de un diccionario
        if isinstance(data, list):
            lista_raw = data
        elif 'relationships_followers' in data:
            lista_raw = data['relationships_followers']
        else:
            lista_raw = data.get('followers', [])
            
        # Extraer los usernames
        followers = set()
        for item in lista_raw:
            for string_data in item.get('string_list_data', []):
                followers.add(string_data.get('value'))
        return followers
    except Exception as e:
        print(f"Error al procesar el archivo de seguidores: {e}")
        sys.exit(1)

def cargar_usuarios_seguidos(ruta_following):
    try:
        with open(ruta_following, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        lista_raw = data.get('relationships_following', [])
        
        following = set()
        for item in lista_raw:
            for string_data in item.get('string_list_data', []):
                following.add(string_data.get('value'))
        return following
    except Exception as e:
        print(f"Error al procesar el archivo de seguidos: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Filtra los usuarios que sigues pero no te siguen de vuelta en Instagram.")
    parser.add_argument('-f', '--followers', required=True, help="Ruta al archivo json de seguidores (ej: followers_1.json)")
    parser.add_argument('-g', '--following', required=True, help="Ruta al archivo json de seguidos (ej: following.json)")
    parser.add_argument('-o', '--output', help="Ruta opcional para guardar el resultado en un archivo de texto")
    
    args = parser.parse_args()
    
    print("🔄 Procesando archivos...")
    followers = cargar_usuarios_seguidores(args.followers)
    following = cargar_usuarios_seguidos(args.following)
    
    # La magia de los sets en Python: los que están en 'following' pero NO en 'followers'
    no_te_siguen = sorted(list(following - followers))
    
    print("\n" + "="*40)
    print(f"📊 RESULTADOS:")
    print(f"👥 Personas que te siguen: {len(followers)}")
    print(f"👉 Personas que seguís: {len(following)}")
    print(f"❌ No te siguen de vuelta: {len(no_te_siguen)}")
    print("="*40 + "\n")
    
    if no_te_siguen:
        print("Usuarios que no te siguen de vuelta:")
        for usuario in no_te_siguen:
            print(f"- {usuario}")
            
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as out_file:
                for usuario in no_te_siguen:
                    out_file.write(f"{usuario}\n")
            print(f"\n💾 Lista guardada con éxito en: {args.output}")
    else:
        print("¡Felicidades! Todos los que seguís te siguen de vuelta. 🎉")

if __name__ == "__main__":
    main()
