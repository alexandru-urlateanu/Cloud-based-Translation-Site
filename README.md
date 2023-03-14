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
5) Website VM image (_afisare-text-tradus.py_)
  - Am creat o imagine pe baza VM-ului pe care am testat aplicația
6) Scale Set
  - Pe baza imaginii VM-ului am definit un scale set 
7) Load Balancer
  - Distribuie traficul venit către IP-ul public al scale set-ului la instanțele de mașini virtuale
