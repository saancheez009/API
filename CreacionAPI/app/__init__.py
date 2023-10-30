
from flask import app

from.periodistas.routes import periodistaBP
from.articulos.routes import articuloBP

app = app(__name__)

# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(periodistaBP, url_prefix='/periodistas')
app.register_blueprint(articuloBP, url_prefix='/articulos')



