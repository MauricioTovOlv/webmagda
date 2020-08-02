from flask  import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/viajes')
def viajes():
    return render_template('viajes.html')

@app.route('/mascaras')
def mascaras():
    return render_template('mascaras.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/foro')
def foro():
    return render_template('foro.html')

@app.route('/ropa')
def ropa():
    return render_template('ropa.html')

@app.route('/preguntas')
def preguntas():
    return render_template('preguntas.html')

if __name__ == '__main__':
    app.run(debug=True)