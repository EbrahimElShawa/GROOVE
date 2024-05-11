from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, GUID
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


# Used to control the system volume
class SystemVolumeController:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(GUID('{5CDF2C82-841E-4546-9722-0CF74078229A}'), CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

    def get_volume(self):
        currentVolumeLevel = self.volume.GetMasterVolumeLevelScalar()
        # Convert to a percentage and return
        return currentVolumeLevel * 100

    def set_volume(self, level):
        volumeLevel = level / 100
        # Set the volume level
        self.volume.SetMasterVolumeLevelScalar(volumeLevel, None)

