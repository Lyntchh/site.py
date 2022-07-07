from flask import Flask, render_template

app = Flask(__name__)

# criar a 1 pagina do site
#rout -> hashtagtreinamentos.com/contatos
# funçao -> oque voçe quer exibir naquela pagina
#template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuario(nome_usuario):
    return nome_usuario

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)