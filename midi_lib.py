import pygame.midi
import time

def play_note(output_device_name, note, velocity, duration):

    midi_device_id = get_midi_out_dev_id_by_name(output_device_name)

    pygame.init()
    pygame.midi.init()
    output = pygame.midi.Output(midi_device_id)
    output.note_on(note, velocity)
    time.sleep(duration)
    output.note_off(note, velocity)
    output.close()
    pygame.midi.quit()

def get_midi_out_dev_id_by_name(midi_device_name):
    names = get_output_midi_devices()
    for i in range(len(names)):
        if names[i]==midi_device_name:
            return i+1
    raise Exception('MIDI device not found : ' + midi_device_name)

def get_output_midi_devices():
    # Initialiser pygame et pygame.midi
    pygame.init()
    pygame.midi.init()

    # Lister les périphériques MIDI disponibles
    output_device_names = []
    for i in range(pygame.midi.get_count()):
        interf, name, input, output, opened = pygame.midi.get_device_info(i)
        if output:
            output_device_names.append( name.decode() )

    # Quitter pygame midi
    pygame.midi.quit()

    return output_device_names
