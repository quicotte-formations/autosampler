import pygame.midi
import time

def play_note(midi_device_id, note, velocity, duration):

    pygame.init()
    pygame.midi.init()
    output = pygame.midi.Output(midi_device_id)
    output.note_on(note, velocity)
    time.sleep(duration)
    output.note_off(note, velocity)
    output.close()
    pygame.midi.quit()

def get_devices_info():
    # Initialiser pygame et pygame.midi
    pygame.init()
    pygame.midi.init()

    # Lister les périphériques MIDI disponibles
    devices_infos = []
    for i in range(pygame.midi.get_count()):
        interf, name, input, output, opened = pygame.midi.get_device_info(i)
        devices_infos.append( {   "id": i,
                                        "interface": interf,
                                        "name": name,
                                        "input": input,
                                        "output": output,
                                        "opened": opened
                                        })

    # Quitter pygame midi
    pygame.midi.quit()

    return devices_infos
