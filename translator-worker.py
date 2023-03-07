import os
import requests
import uuid
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient

storage_account_key = "rb2jORNUeFCT4eQva/oTQC3aC7cR5wmjzlMBrD2T+uLSuZKQX1mA9v1nzNbT+8w9XGVMjKaoGVYg+ASt+Vdf8A=="
storage_account_name = "proiectstorageacc"
connection_string = "DefaultEndpointsProtocol=https;AccountName=proiectstorageacc;AccountKey=rb2jORNUeFCT4eQva" \
                    "/oTQC3aC7cR5wmjzlMBrD2T+uLSuZKQX1mA9v1nzNbT+8w9XGVMjKaoGVYg+ASt+Vdf8A==;EndpointSuffix=core" \
                    ".windows.net "
#
CosmosURI = "https://proiect-cosmo-db.documents.azure.com:443/"
PK = "GF3qiGUTK0UMxYYlrDZsoq0XdrpCo5a6UkVhOXbFXCFrHuMnEjmP2aBguOiaMIHQ7pQXCMiIO4vdACDbJGsn4A=="
connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + storage_account_name + \
              ';AccountKey=' + storage_account_key + ';EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
client = CosmosClient(url=CosmosURI, credential=PK)
#
numeContainerAzure = "proiect-storage-container"
numeContainerCosmos = "Container1"

containerClient = blob_service_client.get_container_client(numeContainerAzure)
# deschidem containerul

database_id = "proiect-container-db"
database_client = client.get_database_client(database_id)
translated_container_client = database_client.get_container_client(numeContainerCosmos)

key = "7e2b61943f4b47f8ab317760a824ed2d"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "francecentral"
path = '/translate'
constructed_url = endpoint + path
varr = "id_text_cosmo"
i = 1


def translate(text, source_language, target_language, key, region, endpoint):
    # Use the Translator translate function
    url = endpoint + "/translate"
    # Build the request
    params = {
        "api-version": "3.0",
        "from": source_language,
        "to": target_language
    }
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json",
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        "text": text
    }]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # Get translation
    translation = response[0]["translations"][0]["text"]
    # Return the translation
    return translation


# def listaBloburi():
#     blobs = containerClient.list_blobs()
#     file_list=[]
#     for blob in containerClient.list_blobs():
#         file_list.append(blob.name)
#     return file_list


blobs = containerClient.list_blobs()
print(blobs)
blob_list = []
for blob in containerClient.list_blobs():
    blob_list.append(blob.name)

print(blob_list)
n = len(blob_list)

while n > 0:
    for fisier in blob_list:
        with open("fisier.txt", "wb") as file:
            file.write(containerClient.download_blob(blob=fisier).readall())
        print("dsa")
        with open("fisier.txt", "r") as file:
            text = file.read()
        textTradus = translate(text, 'en', 'ro', "7e2b61943f4b47f8ab317760a824ed2d",
                               "francecentral", "https://api.cognitive.microsofttranslator.com")
        i = i + 1
        ob_nou = {
            'id_text': varr + str(i),
            "PrimulLimbaj": "Din engleza",
            "Al doilea limbaj": "In romana",
            "textulOriginal": text,
            "TextTradus": textTradus,
            "id": "id_" + str(i)
        }

        try:
            translated_container_client.upsert_item(ob_nou)
        except Exception as e:
            print(e)
        # print(ob_nou)
        n = n - 1
        os.remove("fisier.txt")
