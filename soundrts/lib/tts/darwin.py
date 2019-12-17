"""
This module behaves like pyTTS.
It runs on Mac OS X with NSSpeechSynthesizer.
The only behavior provided is the behavior that tts.py needs.
"""
from __future__ import unicode_literals

from builtins import object
from AppKit import NSSpeechSynthesizer  # @UnresolvedImport


# not used; provided for compatibility
tts_async = 0
tts_purge_before_speak = 0

_engine = NSSpeechSynthesizer.alloc().init()


class TTS(object):

    def __init__(self):
        pass
    
    def IsSpeaking(self):
        return _engine.isSpeaking()

    def Speak(self, text, *args):
        _engine.startSpeakingString_(text)

    def Stop(self):
        _engine.stopSpeaking()


def Create():
    return TTS()
