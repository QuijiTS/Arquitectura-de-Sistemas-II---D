from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import graphene
from flask_graphql import GraphQLView

app = Flask(__name__)
# Usaremos SQLite para no tener que configurar un motor externo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==========================================
# 1. MODELOS DE BASE DE DATOS (SQLAlchemy)
# ==========================================
class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(50))
    libros = db.relationship('Libro', backref='autor', lazy=True)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    paginas = db.Column(db.Integer)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)

# ==========================================
# 2. ESQUEMAS DE GRAPHQL (Graphene)
# ==========================================
class AutorType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    nacionalidad = graphene.String()
    libros = graphene.List(lambda: LibroType)

    def resolve_libros(self, info):
        return Libro.query.filter_by(autor_id=self.id).all()

class LibroType(graphene.ObjectType):
    id = graphene.Int()
    titulo = graphene.String()
    paginas = graphene.Int()
    autor = graphene.Field(AutorType)

    def resolve_autor(self, info):
        return Autor.query.get(self.autor_id)

# ==========================================
# 3. DEFINIR LAS CONSULTAS (Queries)
# ==========================================
class Query(graphene.ObjectType):
    autores = graphene.List(AutorType, description="Obtiene la lista de todos los autores")
    libros = graphene.List(LibroType, description="Obtiene la lista de todos los libros")
    
    def resolve_autores(self, info):
        return Autor.query.all()

    def resolve_libros(self, info):
        return Libro.query.all()

schema = graphene.Schema(query=Query)

# ==========================================
# 4. RUTA DEL ENDPOINT (Sin Autenticación)
# ==========================================
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # ¡CRÍTICO! Esto habilita la interfaz visual
    )
)

# ==========================================
# 5. GENERAR INSTANCIAS (Requisito de la tarea)
# ==========================================
with app.app_context():
    db.create_all()
    # Si no hay autores, creamos datos de prueba automáticamente
    if not Autor.query.first():
        autor1 = Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano")
        autor2 = Autor(nombre="Isaac Asimov", nacionalidad="Ruso-Estadounidense")
        db.session.add_all([autor1, autor2])
        db.session.commit()

        libro1 = Libro(titulo="Cien Años de Soledad", paginas=417, autor_id=autor1.id)
        libro2 = Libro(titulo="Fundación", paginas=255, autor_id=autor2.id)
        db.session.add_all([libro1, libro2])
        db.session.commit()
        print("Base de datos inicializada con datos de prueba.")

if __name__ == '__main__':
    app.run(debug=True)