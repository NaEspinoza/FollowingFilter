# Instagram Unfollowers Tracker 🕵️‍♂️

Una herramienta CLI en Python sencilla y eficiente para descubrir qué usuarios sigues en Instagram que no te siguen de vuelta (*unfollowers*). 

Al procesar los archivos de datos oficiales que Meta te permite descargar, esta herramienta es **100% segura** y garantiza la privacidad de tu cuenta: **no necesitas ingresar tu contraseña, tokens de acceso ni utilizar la API**.

---

## ⚠️ ¿Por qué usar este método?
Las aplicaciones comerciales de la App Store o Play Store que prometen decirte quién no te sigue de forma inmediata acceden a través de "bots" o emuladores utilizando tu contraseña. Instagram cuenta con sistemas sofisticados que **detectan este comportamiento y bloquean o suspenden permanentemente las cuentas** por violar sus términos de servicio. 
Este script lee los datos de forma local en tu computadora, por lo que Instagram nunca sabrá que lo has procesado.

---

## 📋 Requisitos Previos

1. Tener instalado **Python 3.x** o superior.
2. Si vas a utilizar la versión para leer archivos HTML, necesitas instalar la librería `BeautifulSoup4` ejecutando en tu terminal:
    ```bash
    pip install beautifulsoup4

Ó, para mayor facilidad

    pip install -r requirements.txt
---

## 📥 Paso 1: Descargar tus datos de Instagram

Para alimentar al script, necesitas solicitar tus archivos a Meta:

1. Ve a tu perfil de Instagram > **Menú (las tres rayas)** > **Centro de cuentas**.
2. Dirígete a **Tu información y permisos** > **Descargar tu información**.
3. Elige **Descargar o transferir información**.
4. En los tipos de datos, selecciona únicamente **"Seguidores y seguidos"** *(esto hará que Meta genere tu archivo en pocos minutos)*.
5. Elige el formato: puedes elegir **JSON** o **HTML** (tenemos scripts disponibles para ambos formatos).
6. Una vez que te llegue el correo electrónico de Meta, descarga y descomprime el archivo `.zip`.

---

## 🚀 Instrucciones de Uso

Ubica la carpeta descomprimida de Instagram. Los archivos necesarios se encuentran en la ruta interna: `connections/followers_and_following/`.

### Opción A: Si descargaste en formato JSON (Recomendado)

Ejecuta el script `filtrar_unfollowers.py` pasando las rutas a tus archivos `.json`:

```bash
python filtrar_unfollowers.py -f ruta/a/followers_1.json -g ruta/a/following.json

```

### Opción B: Si descargaste en formato HTML

Ejecuta el script `filtrar_html.py` pasando las rutas a tus archivos `.html`:

```bash
python filtrar_html.py -f ruta/a/followers_1.html -g ruta/a/following.html

```

### 💾 Exportar los resultados a un archivo de texto

Si quieres generar una lista limpia en un bloc de notas para ir revisándola después, puedes añadir el argumento `-o` seguido del nombre del archivo:

```bash
python filtrar_html.py -f followers_1.html -g following.html -o lista_para_limpieza.txt

```

---

## 🛠️ Parámetros de la CLI

* `-f`, `--followers`: *(Requerido)* Ruta absoluta o relativa al archivo de seguidores (`followers_1.json` o `followers_1.html`).
* `-g`, `--following`: *(Requerido)* Ruta absoluta o relativa al archivo de seguidos (`following.json` o `following.html`).
* `-o`, `--output`: *(Opcional)* Nombre del archivo de texto de salida donde se guardará la lista filtrada.

---

## 💡 Notas de Soporte

* **¿Qué pasa si el script HTML devuelve 0 usuarios?** Meta suele cambiar esporádicamente el diseño interno y las etiquetas de sus documentos HTML. Si esto te ocurre, te recomendamos solicitar la descarga de datos nuevamente eligiendo el formato **JSON**, cuya estructura de datos es universal y no cambia con actualizaciones visuales.

---
    Para contribuciones, ver [LICENCIA](LICENSE)
    Desarrollado por Nazareno Espinoza
