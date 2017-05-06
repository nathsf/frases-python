from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')
 
@app.route("/hello/<string:name>/", methods=['GET', 'POST'])
def hello(name):
    #    return name
    quotes = [ " Dicen que la suerte surge proporcionalmente a tu sudor. Cuanto más sudes, más suerte encontrarás. Ray Kroc.",
               "La felicidad no se alcanza mediante la inexistencia de problemas, sino enfrentándote a ellos. Steve Maraboli.",
               "La vida es muy simple, pero nos empeñamos en hacerla difícil. Confucio",
               "La vida es una especie de bicicleta. Si quieres mantener el equilibrio, pedalea hacia delante. Albert Einstein.",
               "Aprende de los errores de los demás. No vivirás bastante para cometerlos todos. Groucho Marx.",
               " Una mente independiente no se basa en lo que piensas, sino en cómo piensas. Christopher Hitchens",
               "La riqueza puede medir el talento de uno, pero no su felicidad",
               "El amor de tu vida que siempre has estado buscando esta a tu lado, y si no hay nadie pues busca un gato",
               "Pronto conocerás a alguien importante para ti",
                "Avanza siempre, queriendo tocar el arcoiris con las manos." ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
 
    return render_template('test.html',**locals())

if __name__ == "__main__":
    app.run()