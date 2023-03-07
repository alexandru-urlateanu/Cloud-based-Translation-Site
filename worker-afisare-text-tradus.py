from azure.cosmos import CosmosClient
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    CosmosURI = "https://proiect-cosmo-db.documents.azure.com:443/"
    PK = "GF3qiGUTK0UMxYYlrDZsoq0XdrpCo5a6UkVhOXbFXCFrHuMnEjmP2aBguOiaMIHQ7pQXCMiIO4vdACDbJGsn4A=="
    client = CosmosClient(url=CosmosURI, credential=PK)
    database_name = "proiect-container-db"
    container_name = "Container1"
    database_client = client.get_database_client(database_name)
    container_client = database_client.get_container_client(container_name)
    results = container_client.query_items(query="Select * from c", enable_cross_partition_query=True)
    items = list(results)
    return render_template("fisierIncarcat.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
