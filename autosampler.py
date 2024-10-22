import pygame.midi

import midi_lib
import audio_lib
import threading

devs = midi_lib.get_devices_info()
print( devs )

MIDI_OUT_ID = 3

for note in range(0,128,4):

    # Démarre thread sampling
    ansi_note = pygame.midi.midi_to_ansi_note(note)
    thread_sampling = threading.Thread( target=lambda: audio_lib.sample(1, f'sample-{ansi_note}.wav') )
    thread_sampling.start()

    # Joue note en midi
    midi_lib.play_note(MIDI_OUT_ID, note, 127, 0.5)

    # Attend fin thread sampling
    thread_sampling.join()

