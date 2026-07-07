import os
import argparse
import sys
from bs4 import BeautifulSoup

def extraer_usuarios_html(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print(f"❌ Error: No se encontró el archivo en {ruta_archivo}")
        sys.exit(1)
        
    usuarios = set()
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
            # En el formato HTML de Instagram, los usuarios suelen estar en etiquetas <a> (enlaces)
            # que apuntan a sus perfiles: instagram.com/username
            for enlace in soup.find_all('a'):
                href = enlace.get('href', '')
                texto = enlace.get_text().strip()
                
                # Filtramos para asegurarnos de que sea un usuario y no un enlace cualquiera
                if 'instagram.com' in href and texto and not texto.startswith('http'):
                    usuarios.add(texto)
                # Plan B: Si Instagram cambió el formato, el texto del enlace suele ser el username
                elif texto and not href and not texto.startswith(('http', 'Meta', 'Instagram', 'Inici')):
                    usuarios.add(texto)
                    
        return usuarios
    except Exception as e:
        print(f"Error al procesar {ruta_archivo}: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Filtra unfollowers de Instagram usando archivos HTML.")
    parser.add_argument('-f', '--followers', required=True, help="Ruta al archivo HTML de seguidores (ej: followers_1.html)")
    parser.add_argument('-g', '--following', required=True, help="Ruta al archivo HTML de seguidos (ej: following.html)")
    parser.add_argument('-o', '--output', help="Ruta opcional para guardar el resultado (.txt)")
    
    args = parser.parse_args()
    
    print("🔄 Extrayendo usuarios de los archivos HTML...")
    followers = extraer_usuarios_html(args.followers)
    following = extraer_usuarios_html(args.following)
    
    # Restamos los conjuntos
    no_te_siguen = sorted(list(following - followers))
    
    print("\n" + "="*40)
    print(f"📊 RESULTADOS (Desde HTML):")
    print(f"👥 Personas que te siguen: {len(followers)}")
    print(f"👉 Personas que seguís: {len(following)}")
    print(f"❌ No te siguen de vuelta: {len(no_te_siguen)}")
    print("="*40 + "\n")
    
    if no_te_siguen:
        print("Usuarios que no te siguen:")
        for usuario in no_te_siguen:
            print(f"- {usuario}")
            
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as out_file:
                for usuario in no_te_siguen:
                    out_file.write(f"{usuario}\n")
            print(f"\n💾 Lista guardada en: {args.output}")
    else:
        print("¡Todo en orden! Todos te siguen de vuelta. 🎉")

if __name__ == "__main__":
    main()
