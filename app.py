from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", titulo_pagina="Página inicial")

@app.route("/lista_funcionarios")
def lista_funcionarios():
    return render_template("lista_funcionarios.html", titulo_pagina="lista_funcionarios")

@app.route("/horas_extras")
def horas_extras():
    return render_template("horas_extras.html", titulo_pagina="horas_extras")

@app.route("/Cadastra")
def Cadastra():
    return render_template("paginas/Cadastra.html", titulo_pagina="Cadastra")








if __name__ == "__main__":
    app.run(debug=True)