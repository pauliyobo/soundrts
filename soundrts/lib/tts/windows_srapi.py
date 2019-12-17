"""
This module behaves like pyTTS.
It runs on Windows with ScreenReaderAPI.
The only behavior provided is the behavior that tts.py needs.
"""
from __future__ import unicode_literals

from builtins import object
import ctypes
import time


srapi_wait = .1

# not used; provided for compatibility
tts_async = 0
tts_purge_before_speak = 0

_srapi = ctypes.windll.ScreenReaderAPI


class TTS(object):

    _end_time = None

    def __init__(self):
        _srapi.sapiEnable(1) # fall back to SAPI if no screen reader

    def IsSpeaking(self):
        if self._end_time is None:
            return False
        else:
            return self._end_time > time.time()

    def Speak(self, text, *args):
        _srapi.sayStringW(text, 1)
        self._end_time = time.time() + len(text) * srapi_wait

    def Stop(self):
        _srapi.stopSpeech()
        self._end_time = None


def Create():
    return TTS()
