from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from models.model import Model
from schemas.schema import PersonalitySchema, PersonalityResultSchema, ErrorSchema
from flask_cors import CORS
from sklearn import set_config

info = Info(title="API Classificação de Personalidade", version="1.0.0")
app = OpenAPI(__name__, info=info)
set_config(transform_output="pandas")
CORS(app)

home_tag = Tag(name="Documentação", description="Documentação da API com Swagger")
personality_tag = Tag(name="Personalidade", description="Classificação de personalidade")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

@app.post(
    '/personalidade',
    tags=[personality_tag],
    responses={"200": PersonalityResultSchema, "400": ErrorSchema}
)
def classificar_personalidade(body: PersonalitySchema):
    try:
        model = Model()
        resultado = model.predict_personality(body.model_dump())
        return {"resultado": resultado}, 200
    except Exception as e:
        return {"message": f"Erro ao classificar personalidade: {str(e)}"}, 400

if __name__ == "__main__":
    app.run(debug=True)