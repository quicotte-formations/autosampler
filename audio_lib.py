import pyaudio
import numpy as np
import wave

def sample(sample_dureation_in_seconds, filename):

    # Paramètres de l'enregistrement
    FORMAT = pyaudio.paInt16  # Format de l'échantillonage (16 bits)
    CHANNELS = 2  # Nombre de canaux (1 pour mono, 2 pour stéréo)
    RATE = 44100  # Taux d'échantillonnage (44,1 kHz)
    CHUNK = 1024  # Nombre d'échantillons par chunk (paquet)

    # Initialiser PyAudio
    p = pyaudio.PyAudio()

    # Ouvrir un flux d'entrée audio (microphone ou autre source)
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Enregistrement en cours...")

    # Capturer des données audio (ici, 5 secondes d'enregistrement)
    frames = []
    for i in range(0, int(RATE / CHUNK * sample_dureation_in_seconds)):  # Enregistrement
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))  # Convertir les données en tableau NumPy

    print("Enregistrement terminé.")

    # Fermer le flux et PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Les données audio sont maintenant dans 'frames' (tableau NumPy)
    # Par exemple, vous pouvez les analyser ou les sauvegarder en fichier .wav

    # Optionnel : convertir en un grand tableau NumPy pour traitement
    audio_data = np.hstack(frames)

    # Exemple d'accès aux données : afficher les 10 premiers échantillons
    print(audio_data[:10])

    # Sauvegarder les données audio dans un fichier .wav
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join([frame.tobytes() for frame in frames]))
    wf.close()

    print(f"Fichier sauvegardé sous {filename}")