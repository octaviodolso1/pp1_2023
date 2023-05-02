from flask import Flask, render_template
app = Flask (__name__)

@app.route("/")
def index():
    mensajedebienvenida = "hola bienvenido a Flask"
    carreras = ['Desarrollo de Software',
                'Tec. en Electromecanica',
                'Turismo',
            ]
    return render_template(
        "index.html",
        mensaje = mensajedebienvenida,
        lista_carreras = carreras,
        )

@app.route("/bienvenido")
def bienvenida():
    return "<h3 Style=color:blue> Bienvenido a Flask</h3>"

@app.route("/bienvenido/<nombre>")
def bienvenida_con_nombre(nombre):
    return "<h3 Style=color:blue> bienvenido {nombre} a Flask</h3>"

@app.route("/suma/<a>/<b>")
def suma(a,b):
    try:
        a=int(a)
        b=int(b)
        suma = a + b
        int(a) and int (b) 
        return f"<h1>{suma}</h1>"
    except:
        return("Por favor envia numeros con parametros")

