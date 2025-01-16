import pyautogui
import random
import time
import keyboard  # Bibliothèque pour détecter les combinaisons de touches

def auto_clicker(min_delay, max_delay, min_pause_interval, max_pause_interval, min_pause_duration, max_pause_duration):
    """
    Auto-clicker avec des délais aléatoires entre les clics et des pauses aléatoires.
    :param min_delay: Délai minimum entre deux clics (en secondes).
    :param max_delay: Délai maximum entre deux clics (en secondes).
    :param min_pause_interval: Intervalle minimum entre deux pauses (en secondes).
    :param max_pause_interval: Intervalle maximum entre deux pauses (en secondes).
    :param min_pause_duration: Durée minimale d'une pause (en secondes).
    :param max_pause_duration: Durée maximale d'une pause (en secondes).
    """
    print("Auto-clicker démarré. Appuyez sur Ctrl+Y pour arrêter.")
    
    # Définit un intervalle de pause initial aléatoire
    next_pause_interval = random.uniform(min_pause_interval, max_pause_interval)
    start_time = time.time()  # Enregistre le temps de début


    
    try:
        while True:
            # Vérifie si l'utilisateur a appuyé sur Ctrl+Y
            if keyboard.is_pressed('ctrl+y'):
                print("Auto-clicker arrêté par l'utilisateur via Ctrl+Y.")
                break
            
            # Effectue un clic gauche
            pyautogui.click()
            print("Clic effectué.")
            
            # Vérifie si une pause doit être effectuée
            elapsed_time = time.time() - start_time
            if elapsed_time >= next_pause_interval:
                pause_duration = random.uniform(min_pause_duration, max_pause_duration)
                print(f"Pause de {pause_duration:.2f} secondes après {elapsed_time:.2f} secondes de clics.")
                time.sleep(pause_duration)

                # Vérifie si l'utilisateur a appuyé sur Ctrl+Y
                if keyboard.is_pressed('ctrl+y'):
                    print("Auto-clicker arrêté par l'utilisateur via Ctrl+Y.")
                    break
                
                # Réinitialise le temps de début et calcule un nouveau délai avant la prochaine pause
                start_time = time.time()
                next_pause_interval = random.uniform(min_pause_interval, max_pause_interval)
                print(f"Prochaine pause prévue dans {next_pause_interval:.2f} secondes.")
            
            # Génère un délai aléatoire avant le prochain clic
            delay = random.uniform(min_delay, max_delay)
            print(f"Prochain clic dans {delay:.2f} secondes.")
            
            # Pause avant le prochain clic
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Auto-clicker arrêté par l'utilisateur (Ctrl+C).")

# Configuration des délais aléatoires (en secondes)
min_delay = 0.02492  # Délai minimum entre deux clics
max_delay = 0.03189  # Délai maximum entre deux clics
min_pause_interval = 31.82  # Intervalle minimum entre deux pauses (en secondes)
max_pause_interval = 46.76  # Intervalle maximum entre deux pauses (en secondes)
min_pause_duration = 5.8906  # Durée minimale d'une pause (en secondes)
max_pause_duration = 13.501  # Durée maximale d'une pause (en secondes)

# Démarre l'auto-clicker
auto_clicker(min_delay, max_delay, min_pause_interval, max_pause_interval, min_pause_duration, max_pause_duration)
