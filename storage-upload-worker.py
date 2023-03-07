import os
from azure.storage.blob import BlobServiceClient

storage_account_key = "rb2jORNUeFCT4eQva/oTQC3aC7cR5wmjzlMBrD2T+uLSuZKQX1mA9v1nzNbT+8w9XGVMjKaoGVYg+ASt+Vdf8A=="
storage_account_name = "proiectstorageacc"
connection_string = "DefaultEndpointsProtocol=https;AccountName=proiectstorageacc;AccountKey=rb2jORNUeFCT4eQva" \
                    "/oTQC3aC7cR5wmjzlMBrD2T+uLSuZKQX1mA9v1nzNbT+8w9XGVMjKaoGVYg+ASt+Vdf8A==;EndpointSuffix=core" \
                    ".windows.net"
container_name = "proiect-storage-container"

# BlobServiceClient.from_connection_string utilizat pentru a accesa serviciul de stocare BLOB
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

path = 'D:\\FACULTATE\\ANUL 3\\SEM 1\\Cloud Computing\\PROIECT\\data'
for filename in os.listdir(path):
    full_path = os.path.join(path, filename)
    if os.path.isfile(full_path):
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
        with open(file=full_path, mode="rb") as data:
            blob_client.upload_blob(data)
