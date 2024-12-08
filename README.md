# various central players for the SQUIM project

## files

- *.mada songs, - either handwritten through chords or converted from MXL
- *.mxl - public domain MXL music scores
- generated_tlv.py - code snipped generated from [squim_tlv_generator ](https://github.com/wenzellabs/squim_tlv_generator)
- mada_player - central player for mada formatted songs, the thing you're looking for to run
- midi_player - can play MIDI files on SQUIM nodes, with bonus features when a UDP note_off gets lost in the ether
- mxl2mada - converter from MXL formatted songs, wild and experimental
- PANIC - STOP ALL AUDIO NOW!1!
- shepard - toy experiment presenting a minimal SQUIM API

## how

put some SQUIM nodes into one WiFi, join the same WiFi with a computer, and run `mada_player -r *.mada`
