# this stuff is automagically generated from
# tlv_generator.py - do not edit

import struct
from enum import Enum

MAESTRO_PORT = 11000 # UDP port

# base TLV Packet class
class TLVPacket:
    def __init__(self, type, payload):
        self.type = type
        self.len = 2 + len(payload)  # header length is 2 bytes
        self.payload = payload

    def to_bytes(self):
        header = struct.pack('<BB', self.type, self.len)
        return header + self.payload

    @staticmethod
    def from_bytes(data):
        type, length = struct.unpack('<BB', data[:2])
        payload = data[2:length]
        return TLVPacket(type, payload)


# derived classes for specific TLV types

class TLVPacketTime(TLVPacket):
    def __init__(self, us_since_1900):
        tlv_nonce = 0x01
        payload = struct.pack('<Q', us_since_1900)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        us_since_1900, = struct.unpack('<Q', data[2:])
        return TLVPacketTime(us_since_1900, )

class TLVPacketNoteOn(TLVPacket):
    def __init__(self, us_since_1900, note, channel, velocity):
        tlv_nonce = 0x11
        payload = struct.pack('<QBBB', us_since_1900, note, channel, velocity)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        us_since_1900, note, channel, velocity, = struct.unpack('<QBBB', data[2:])
        return TLVPacketNoteOn(us_since_1900, note, channel, velocity, )

class TLVPacketNoteOff(TLVPacket):
    def __init__(self, us_since_1900, note, channel, velocity):
        tlv_nonce = 0x12
        payload = struct.pack('<QBBB', us_since_1900, note, channel, velocity)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        us_since_1900, note, channel, velocity, = struct.unpack('<QBBB', data[2:])
        return TLVPacketNoteOff(us_since_1900, note, channel, velocity, )

class TLVPacketNoteOnOff(TLVPacket):
    def __init__(self, on, off, note, channel, velocity):
        tlv_nonce = 0x13
        payload = struct.pack('<QQBBB', on, off, note, channel, velocity)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        on, off, note, channel, velocity, = struct.unpack('<QQBBB', data[2:])
        return TLVPacketNoteOnOff(on, off, note, channel, velocity, )

class TLVPacketPanic(TLVPacket):
    def __init__(self):
        tlv_nonce = 0x1f
        payload = b''
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        return TLVPacketPanic()

class TLVPacketBeat(TLVPacket):
    def __init__(self, bpm, count):
        tlv_nonce = 0x20
        payload = struct.pack('<BI', bpm, count)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        bpm, count, = struct.unpack('<BI', data[2:])
        return TLVPacketBeat(bpm, count, )

class TLVPacketStart(TLVPacket):
    def __init__(self, us_since_1900, bpm, count):
        tlv_nonce = 0x21
        payload = struct.pack('<QBI', us_since_1900, bpm, count)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        us_since_1900, bpm, count, = struct.unpack('<QBI', data[2:])
        return TLVPacketStart(us_since_1900, bpm, count, )

class TLVPacketKeyNotes(TLVPacket):
    def __init__(self, root, third, fifth, seventh, ninth, eleventh, thirteenth):
        tlv_nonce = 0x30
        payload = struct.pack('<BBBBBBB', root, third, fifth, seventh, ninth, eleventh, thirteenth)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        root, third, fifth, seventh, ninth, eleventh, thirteenth, = struct.unpack('<BBBBBBB', data[2:])
        return TLVPacketKeyNotes(root, third, fifth, seventh, ninth, eleventh, thirteenth, )

class TLVPacketChord(TLVPacket):
    def __init__(self, on, off, note):
        tlv_nonce = 0x31
        payload = struct.pack('<QQ16B', on, off, *note)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        on, off, *note, = struct.unpack('<QQ16B', data[2:])
        return TLVPacketChord(on, off, note, )

class TLVPacketScale(TLVPacket):
    Enum_scale_type = Enum('Enum_scale_type', ['major', 'minor', 'harmonic_minor', 'melodic_minor', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'locrian', 'major_pentatonic', 'minor_pentatonic', 'blues_minor', 'blues_major', 'whole_tone', 'chromatic'])
    def __init__(self, root, scale_type):
        tlv_nonce = 0x32
        payload = struct.pack('<BB', root, scale_type.value)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        root, scale_type, = struct.unpack('<BB', data[2:])
        return TLVPacketScale(root, scale_type, )

class TLVPacketArtist(TLVPacket):
    def __init__(self, artist):
        tlv_nonce = 0x23
        payload = struct.pack('<234b', *artist)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        *artist, = struct.unpack('<234b', data[2:])
        return TLVPacketArtist(artist, )

class TLVPacketTitle(TLVPacket):
    def __init__(self, title):
        tlv_nonce = 0x24
        payload = struct.pack('<234b', *title)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        *title, = struct.unpack('<234b', data[2:])
        return TLVPacketTitle(title, )

class TLVPacketLedColor(TLVPacket):
    def __init__(self, led, r, g, b):
        tlv_nonce = 0x40
        payload = struct.pack('<BBBB', led, r, g, b)
        super().__init__(tlv_nonce, payload)

    @staticmethod
    def from_bytes(data):
        led, r, g, b, = struct.unpack('<BBBB', data[2:])
        return TLVPacketLedColor(led, r, g, b, )


# end of automagically generated code
