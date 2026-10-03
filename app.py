import json
import os
import unicodedata
from flask import Flask, render_template, request, abort

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "problems.json")

with open(DATA_PATH, encoding="utf-8") as f:
    PROBLEMS = json.load(f)

PROBLEMS_BY_ID = {p["id"]: p for p in PROBLEMS}
PROBLEMS_BY_SLUG = {p["slug"]: p for p in PROBLEMS}

SISTEMAS_PC = ["Windows", "macOS", "Linux"]
SISTEMAS_CELULAR = ["Android", "iOS"]

ICONOS_SISTEMA = {
    "Windows": "🪟",
    "macOS": "🍎",
    "Linux": "🐧",
    "Android": "🤖",
    "iOS": "📱",
    "General": "🛠️",
}

ICONOS_CATEGORIA = {
    "Rendimiento": "⚡",
    "Aplicaciones": "📦",
    "Actualizaciones": "🔄",
    "Periféricos": "🖱️",
    "Sonido": "🔊",
    "Internet": "🌐",
    "Inicio del sistema": "🔌",
    "Archivos": "📁",
    "Impresoras": "🖨️",
    "Seguridad": "🛡️",
    "Sistema operativo": "💻",
    "Almacenamiento": "💾",
    "Bluetooth": "📶",
    "Cámara": "📷",
    "Batería": "🔋",
    "Pantalla": "🖥️",
    "Configuración": "⚙️",
    "Cuentas y sesiones": "👤",
    "Dispositivos externos": "🔌",
    "Navegadores": "🧭",
}


def icono_sistema(sistema):
    return ICONOS_SISTEMA.get(sistema, "🛠️")


def icono_categoria(categoria):
    return ICONOS_CATEGORIA.get(categoria, "🔧")


app.jinja_env.globals.update(
    icono_sistema=icono_sistema,
    icono_categoria=icono_categoria,
)


def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto


PALABRAS_VACIAS = {
    "mi", "tu", "su", "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "al", "a", "en", "no", "se", "que", "con", "por", "para",
    "esta", "esto", "estan", "estas", "estos", "es", "son", "muy", "mas",
    "y", "o", "pero", "como", "cuando", "donde", "lo", "le", "les", "lo que",
    "tiene", "tengo", "tienes", "hay", "ya", "me", "yo", "porque", "sin",
}

SINONIMOS_SISTEMA = {
    "pc": ["Windows", "macOS", "Linux"],
    "computador": ["Windows", "macOS", "Linux"],
    "computadora": ["Windows", "macOS", "Linux"],
    "ordenador": ["Windows", "macOS", "Linux"],
    "notebook": ["Windows", "macOS", "Linux"],
    "laptop": ["Windows", "macOS", "Linux"],
    "celular": ["Android", "iOS"],
    "telefono": ["Android", "iOS"],
    "movil": ["Android", "iOS"],
    "smartphone": ["Android", "iOS"],
    "iphone": ["iOS"],
    "ios": ["iOS"],
    "android": ["Android"],
    "windows": ["Windows"],
    "mac": ["macOS"],
    "macbook": ["macOS"],
    "macos": ["macOS"],
    "linux": ["Linux"],
    "ubuntu": ["Linux"],
}


def obtener_categorias(sistema=None):
    problemas = PROBLEMS
    if sistema:
        problemas = [p for p in PROBLEMS if p["sistema"] == sistema]
    categorias = sorted(set(p["categoria"] for p in problemas))
    return categorias


def buscar_problemas(consulta):
    consulta_norm = normalizar(consulta.strip())
    if not consulta_norm:
        return []

    palabras_consulta = [w for w in consulta_norm.split() if w]
    palabras_utiles = [w for w in palabras_consulta if w not in PALABRAS_VACIAS]
    if not palabras_utiles:
        palabras_utiles = palabras_consulta

    sistemas_sugeridos = set()
    for palabra in palabras_utiles:
        if palabra in SINONIMOS_SISTEMA:
            sistemas_sugeridos.update(SINONIMOS_SISTEMA[palabra])

    def coincide(palabra, texto):
        if len(palabra) <= 4:
            return palabra in texto
        raiz = palabra[:4]
        return raiz in texto

    resultados = []
    for p in PROBLEMS:
        titulo_norm = normalizar(p["titulo"])
        categoria_norm = normalizar(p["categoria"])
        sistema_norm = normalizar(p["sistema"])
        descripcion_norm = normalizar(p["descripcion"])
        palabras_clave_norm = normalizar(" ".join(p["palabras_clave"]))

        texto_indexado = " ".join(
            [titulo_norm, descripcion_norm, categoria_norm, sistema_norm, palabras_clave_norm]
        )

        puntaje = 0

        if consulta_norm in texto_indexado:
            puntaje += 10
        if consulta_norm in titulo_norm:
            puntaje += 10

        for palabra in palabras_utiles:
            if coincide(palabra, palabras_clave_norm):
                puntaje += 4
            if coincide(palabra, titulo_norm):
                puntaje += 5
            if coincide(palabra, categoria_norm):
                puntaje += 3
            if coincide(palabra, sistema_norm):
                puntaje += 3
            if coincide(palabra, descripcion_norm):
                puntaje += 1

        if p["sistema"] in sistemas_sugeridos:
            puntaje += 6

        if puntaje > 0:
            resultados.append((puntaje, p))

    resultados.sort(key=lambda x: x[0], reverse=True)
    return [p for _puntaje, p in resultados]




@app.route("/")
def inicio():
    # Selección de problemas frecuentes reales representativos
    ids_frecuentes = [1, 108, 21, 15, 63, 65]
    problemas_frecuentes = [
        PROBLEMS_BY_ID[pid] for pid in ids_frecuentes if pid in PROBLEMS_BY_ID
    ]
    return render_template("index.html", problemas_frecuentes=problemas_frecuentes)


@app.route("/buscar")
def buscar():
    consulta = request.args.get("q", "").strip()
    resultados = buscar_problemas(consulta) if consulta else []
    return render_template("buscar.html", consulta=consulta, resultados=resultados)


@app.route("/pc")
def pc():
    sistema = request.args.get("sistema", "")
    categoria = request.args.get("categoria", "")

    problemas = [p for p in PROBLEMS if p["sistema"] in SISTEMAS_PC]

    if sistema:
        problemas = [p for p in problemas if p["sistema"] == sistema]

    categorias_disponibles = obtener_categorias(sistema) if sistema else []

    if categoria:
        problemas = [p for p in problemas if p["categoria"] == categoria]

    return render_template(
        "pc.html",
        sistemas=SISTEMAS_PC,
        sistema_seleccionado=sistema,
        categorias=categorias_disponibles,
        categoria_seleccionada=categoria,
        problemas=problemas,
    )


@app.route("/celulares")
def celulares():
    sistema = request.args.get("sistema", "")
    categoria = request.args.get("categoria", "")

    problemas = [p for p in PROBLEMS if p["sistema"] in SISTEMAS_CELULAR]

    if sistema:
        problemas = [p for p in problemas if p["sistema"] == sistema]

    categorias_disponibles = obtener_categorias(sistema) if sistema else []

    if categoria:
        problemas = [p for p in problemas if p["categoria"] == categoria]

    return render_template(
        "celulares.html",
        sistemas=SISTEMAS_CELULAR,
        sistema_seleccionado=sistema,
        categorias=categorias_disponibles,
        categoria_seleccionada=categoria,
        problemas=problemas,
    )


@app.route("/diagnostico", methods=["GET", "POST"])
def diagnostico():
    tipo_dispositivo = request.values.get("dispositivo", "")
    sistema = request.values.get("sistema", "")
    categoria = request.values.get("categoria", "")

    sistemas_disponibles = []
    if tipo_dispositivo == "pc":
        sistemas_disponibles = SISTEMAS_PC
    elif tipo_dispositivo == "celular":
        sistemas_disponibles = SISTEMAS_CELULAR

    categorias_disponibles = obtener_categorias(sistema) if sistema else []

    resultados = []
    if tipo_dispositivo and sistema and categoria:
        resultados = [
            p
            for p in PROBLEMS
            if p["sistema"] == sistema and p["categoria"] == categoria
        ]
    elif tipo_dispositivo and sistema:
        resultados = [p for p in PROBLEMS if p["sistema"] == sistema]

    return render_template(
        "diagnostico.html",
        tipo_dispositivo=tipo_dispositivo,
        sistema=sistema,
        categoria=categoria,
        sistemas_disponibles=sistemas_disponibles,
        categorias_disponibles=categorias_disponibles,
        resultados=resultados,
    )


@app.route("/problema/<slug>")
def problema(slug):
    p = PROBLEMS_BY_SLUG.get(slug)
    if not p:
        abort(404)

    relacionados = [
        PROBLEMS_BY_ID[rid] for rid in p["relacionados"] if rid in PROBLEMS_BY_ID
    ]

    return render_template("problema.html", p=p, relacionados=relacionados)


@app.route("/herramientas")
def herramientas():
    return render_template("herramientas.html")


@app.route("/mantenimiento")
def mantenimiento():
    return render_template("mantenimiento.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")




@app.errorhandler(404)
def pagina_no_encontrada(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
