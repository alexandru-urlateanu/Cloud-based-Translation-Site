import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField

load_dotenv()

# GET- metoda pentru a obtine informatii de la server(in cazul nostru fisiere.txt)
# POST- trimitem informatii catre server(fisiere traduse)
# @app.route este o funcție din pachetul Flask care este utilizată pentru a genera un răspuns HTTP, care conține o pagină web
# "/" este ruta

app = Flask(__name__)
# trebuie sa cream o cheie secreta ca form-ul sa apara in templates
# trebuie sa folosim o cheie secreta ca sa folosim csrf token care vine cu form-ul
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'data'


# cream form-ul
class UploadFileForm(FlaskForm):
    # cream input field-ul
    file = FileField("File")
    # cream butonul de submit
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():  # o data ce dam submit la fisier:
        file = form.file.data  # Prima data luam fisierul
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))  # Then save the file
        return "Fisierul a fost incarcat!"
    return render_template('index.html', form=form)


# @app.route('/fisiereTranslatate', methods=['GET'])
# def translatat():
#     CosmosURI = "https://proiect-cosmo-db.documents.azure.com:443/"
#     PK = "GF3qiGUTK0UMxYYlrDZsoq0XdrpCo5a6UkVhOXbFXCFrHuMnEjmP2aBguOiaMIHQ7pQXCMiIO4vdACDbJGsn4A=="
#     client = CosmosClient(url=CosmosURI, credential=PK)
#     database = client.create_database_if_not_exists(id="proiect-container-db")
#     container = database.create_container_if_not_exists(id="Container1", partition_key='/id_text')
#     query = "SELECT * from fisiere"
#     items = container.query_items(query=query, enable_cross_partiton_query=True)
#     return render_template('/fisiereTranslatate', texts=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
