import speech_recognition as sr
# Assurez-vous que le module `reponses` et la fonction `generer_reponse_ia` sont correctement définis
from reponses import generer_reponse_ia  

def ecouter_et_repondre():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Je vous écoute...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustement pour le bruit ambiant
        audio = recognizer.listen(source)

        try:
            # Reconnaissance de la parole en français
            text = recognizer.recognize_google(audio, language='fr-FR')
            print(f"Vous avez dit: {text}")

            # Générer une réponse appropriée
            reponse = generer_reponse_ia(text)
            print(f"Réponse générée: {reponse}")

        except sr.UnknownValueError:
            print("Je n'ai pas compris. Veuillez répéter.")
        except sr.RequestError as e:
            print(f"Erreur de service; {e}")

if __name__ == "__main__":
    ecouter_et_repondre()
