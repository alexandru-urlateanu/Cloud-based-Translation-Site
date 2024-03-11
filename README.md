# Cloud Computing Project
## Site de traducere texte din limba engleză în limba română, bazat pe servicii Microsoft Azure
#### Scopul realizării proiectului a fost folosirea a cât mai multor servicii Microsoft Azure și înțelegerea modurilor de funcționare a acestora

__Componente__
1) Website de încărcare a fișierelor (_app.py_)
  - Este găzduit pe o mașină virtuală din Microsoft Azure
  - Rulează prin intermediul unei aplicații Flask
  - Preia fișierelor .txt din sistemul utilizatorului și le încarcă în aplicație
  - Va rula pe portul 5000
2) Script-ul _storage-upload.py_ preia fișierele text din aplicație și le încarcă într-un container de **Azure Storage** sub forma unor BLOB-uri.
3) Script-ul _translator.py_ se folosește de **Azure Cognitive Services Translator** pentru a realiza traducerea textelor, urmând să încarce fișierele traduse într-o bază de date **Azure Cosmos DB**
4) Website pentru afișarea rezultatelor
  - Rulează prin intermediul unei aplicații Flask ce va prelua textele traduse din baza de date Cosmos DB și va afișa pe pagină atât textele originale, cât și pe cele translatate
  - Va rula pe portul 5001
5) Website VM image
  - Am creat o imagine pe baza VM-ului pe care am testat aplicația
6) Scale Set
  - Pe baza imaginii VM-ului am definit un scale set 
7) Load Balancer
  - Distribuie traficul venit către IP-ul public al scale set-ului la instanțele de mașini virtuale

# (ENGLISH) Cloud Computing Project
## Text translation site from English to Romanian, based on Microsoft Azure services
#### The goal of the project was to use as many Microsoft Azure services as possible and to understand how they work

__Components__
1) File Upload Website (_app.py_)
   - It is hosted on a virtual machine in Microsoft Azure
   - Runs via a Flask app
   - Retrieves .txt files from the user's system and uploads them to the application
   - It will run on port 5000
2) The _storage-upload.py_ script takes the text files from the application and uploads them to an **Azure Storage** container as BLOBs.
3) The _translator.py_ script is used by **Azure Cognitive Services Translator** to translate the texts, then upload the translated files to an **Azure Cosmos DB** database
4) Website for displaying the results
   - Runs through a Flask application that will retrieve the translated texts from the Cosmos DB database and display both the original and the translated texts on the page
   - It will run on port 5001
5) Website VM image
   - I created an image based on the VM on which I tested the application
6) Scale Set
   - Based on the VM image we defined a scale set
7) Load Balancer
   - Distributes incoming traffic to the public IP of the scale set to the VM instances
