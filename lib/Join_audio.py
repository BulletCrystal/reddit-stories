def coller_fichiers_audio(fichiers_sources, fichier_destination):
  """
  Concatène plusieurs fichiers audio dans un seul fichier destination.

  Args:
      fichiers_sources: Une liste de chemins d'accès aux fichiers audio sources.
      fichier_destination: Le chemin d'accès au fichier audio destination.
  """
  with open(fichier_destination, 'wb') as destination:
    for fichier_source in fichiers_sources:
      with open(fichier_source, 'rb') as source:
        destination.write(source.read())

# Exemple d'utilisation
fichiers_sources = ["./Audios/output0.mp3", "./Audios/output1.mp3","./Audios/output2.mp3", "./Audios/output3.mp3"]
fichier_destination = "FINALE.mp3"
coller_fichiers_audio(fichiers_sources, fichier_destination)
