import midi_lib

devs = midi_lib.get_output_midi_devices()
print( devs )

DEVICE = 'UM-ONE'
port = midi_lib.get_midi_out_dev_id_by_name( DEVICE )

while True:
    for note in range(0,128,3):
        midi_lib.play_note(DEVICE, note, 127, 0.1)
    for note in range(127,-1, -3):
        midi_lib.play_note(DEVICE, note, 127, 0.1)