#!/usr/bin/env python3

import sys
import mido
import time
import socket
from generated_tlv import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

SQUIM_PORT = 11000

# calculate microseconds since 1900
def get_us_since_1900():
    NTP_DELTA = 2208988800  # seconds between 1900 and 1970
    current_time = time.time()  # seconds since epoch (1970)
    us_since_1900 = int((current_time + NTP_DELTA) * 1e6)  # convert to us since 1900
    return us_since_1900

def create_note_packet(event, current_time_us):
    note = event.note
    ch = event.channel
    velo = event.velocity
    if event.type == 'note_on':
        print(f'note on  {note}')
        return TLVPacketNoteOn(current_time_us, note, ch, velo)
    elif event.type == 'note_off':
        print(f'note off {note}')
        return TLVPacketNoteOff(current_time_us, note, ch, velo)
    else:
        return None

def send_tlv_packet(packet):
    sock.sendto(packet.to_bytes(), ('255.255.255.255', SQUIM_PORT))

# load a MIDI file
midi_file_path = 'your_file.mid'  # default
if len(sys.argv) > 1:
    midi_file_path = sys.argv[1]

midi_file = mido.MidiFile(midi_file_path)

# extract BPM from MIDI file (assume tempo in first track)
bpm = int(mido.tempo2bpm(mido.MetaMessage('set_tempo', tempo=500000).tempo))

# send initial time packet
current_time_us = get_us_since_1900()
tlv_time = TLVPacketTime(current_time_us)
send_tlv_packet(tlv_time)

for _ in range(3):
    send_tlv_packet(TLVPacketPanic())
    time.sleep(.1)

# Announce the start of the song
start_time_us = get_us_since_1900()
tlv_start = TLVPacketStart(start_time_us, bpm, count=0)
send_tlv_packet(tlv_start)

# init beat count
beat_count = 0
next_beat_time_us = start_time_us

note_delay = 3 * 1000 * 1000

# play the MIDI file
start_playback_time_us = get_us_since_1900()
for message in midi_file.play():
    current_time_us = get_us_since_1900()
    
    # send beat packet at each beat
    if current_time_us >= next_beat_time_us:
        tlv_beat = TLVPacketBeat(bpm, beat_count)
        send_tlv_packet(tlv_beat)
        print(f'beat {beat_count}')
        beat_count += 1
        next_beat_time_us += int(60.0 / bpm * 1e6)  # Schedule next beat in microseconds
        send_tlv_packet(TLVPacketPanic())
    
    # handle note on/off events
    if message.type in ['note_on', 'note_off']:
        tlv_packet = create_note_packet(message, current_time_us + note_delay)
        if tlv_packet:
            send_tlv_packet(tlv_packet)

sock.close()
