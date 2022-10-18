#: *****************************************************************************
#:                    The code in this file was created by Ratul Hasan         *
#:                     So comlpete credit goes to him(me)                      *
#:                  comtypes Librarys are used in this code                    *
#: *****************************************************************************
#: Sharing this code without my permission is not allowed                      *
#: *****************************************************************************
#: This code was created based on IDLE, Pydroid(Android), qPython(Android) etc.*
#: So most online/web site based idle(i.e: Sololearn) can't run this code      *
#: properly.                                                                   *
#: *****************************************************************************
#: If there is any bug or you want to help please let me know.                 *
#: e-mail: wwwqweasd147[at]gmail[dot]com                                       *
#: *****************************************************************************



from os import name as os_name
import random
from sys	import getfilesystemencoding
#from time import sleep
import ctypes
import comtypes
from ctypes import wintypes

MMDeviceApiLib = comtypes.GUID(
    '{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}')
IID_IMMDevice = comtypes.GUID(
    '{D666063F-1587-4E43-81F1-B948E807363F}')
IID_IMMDeviceCollection = comtypes.GUID(
    '{0BD7A1BE-7A1A-44DB-8397-CC5392387B5E}')
IID_IMMDeviceEnumerator = comtypes.GUID(
    '{A95664D2-9614-4F35-A746-DE8DB63617E6}')
IID_IAudioEndpointVolume = comtypes.GUID(
    '{5CDF2C82-841E-4546-9722-0CF74078229A}')
CLSID_MMDeviceEnumerator = comtypes.GUID(
    '{BCDE0395-E52F-467C-8E3D-C4579291692E}')

# EDataFlow
eRender = 0 # audio rendering stream
eCapture = 1 # audio capture stream
eAll = 2 # audio rendering or capture stream

# ERole
eConsole = 0 # games, system sounds, and voice commands
eMultimedia = 1 # music, movies, narration
eCommunications = 2 # voice communications

LPCGUID = REFIID = ctypes.POINTER(comtypes.GUID)
LPFLOAT = ctypes.POINTER(ctypes.c_float)
LPDWORD = ctypes.POINTER(wintypes.DWORD)
LPUINT = ctypes.POINTER(wintypes.UINT)
LPBOOL = ctypes.POINTER(wintypes.BOOL)
PIUnknown = ctypes.POINTER(comtypes.IUnknown)

class IMMDevice(comtypes.IUnknown):
    _iid_ = IID_IMMDevice
    _methods_ = (
        comtypes.COMMETHOD([], ctypes.HRESULT, 'Activate',
            (['in'], REFIID, 'iid'),
            (['in'], wintypes.DWORD, 'dwClsCtx'),
            (['in'], LPDWORD, 'pActivationParams', None),
            (['out','retval'], ctypes.POINTER(PIUnknown), 'ppInterface')),
        comtypes.STDMETHOD(ctypes.HRESULT, 'OpenPropertyStore', []),
        comtypes.STDMETHOD(ctypes.HRESULT, 'GetId', []),
        comtypes.STDMETHOD(ctypes.HRESULT, 'GetState', []))

PIMMDevice = ctypes.POINTER(IMMDevice)

class IMMDeviceCollection(comtypes.IUnknown):
    _iid_ = IID_IMMDeviceCollection

PIMMDeviceCollection = ctypes.POINTER(IMMDeviceCollection)

class IMMDeviceEnumerator(comtypes.IUnknown):
    _iid_ = IID_IMMDeviceEnumerator
    _methods_ = (
        comtypes.COMMETHOD([], ctypes.HRESULT, 'EnumAudioEndpoints',
            (['in'], wintypes.DWORD, 'dataFlow'),
            (['in'], wintypes.DWORD, 'dwStateMask'),
            (['out','retval'], ctypes.POINTER(PIMMDeviceCollection),
             'ppDevices')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetDefaultAudioEndpoint',
            (['in'], wintypes.DWORD, 'dataFlow'),
            (['in'], wintypes.DWORD, 'role'),
            (['out','retval'], ctypes.POINTER(PIMMDevice), 'ppDevices')))
    @classmethod
    def get_default(cls, dataFlow, role):
        enumerator = comtypes.CoCreateInstance(
            CLSID_MMDeviceEnumerator, cls, comtypes.CLSCTX_INPROC_SERVER)
        return enumerator.GetDefaultAudioEndpoint(dataFlow, role)

class IAudioEndpointVolume(comtypes.IUnknown):
    _iid_ = IID_IAudioEndpointVolume
    _methods_ = (
        comtypes.STDMETHOD(ctypes.HRESULT, 'RegisterControlChangeNotify', []),
        comtypes.STDMETHOD(ctypes.HRESULT, 'UnregisterControlChangeNotify', []),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetChannelCount',
            (['out', 'retval'], LPUINT, 'pnChannelCount')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'SetMasterVolumeLevel',
            (['in'], ctypes.c_float, 'fLevelDB'),
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'SetMasterVolumeLevelScalar',
            (['in'], ctypes.c_float, 'fLevel'),
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetMasterVolumeLevel',
            (['out','retval'], LPFLOAT, 'pfLevelDB')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetMasterVolumeLevelScalar',
            (['out','retval'], LPFLOAT, 'pfLevel')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'SetChannelVolumeLevel',
            (['in'], wintypes.UINT, 'nChannel'),
            (['in'], ctypes.c_float, 'fLevelDB'),
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'SetChannelVolumeLevelScalar',
            (['in'], wintypes.UINT, 'nChannel'),
            (['in'], ctypes.c_float, 'fLevel'),
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetChannelVolumeLevel',
            (['in'], wintypes.UINT, 'nChannel'),
            (['out','retval'], LPFLOAT, 'pfLevelDB')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetChannelVolumeLevelScalar',
            (['in'], wintypes.UINT, 'nChannel'),
            (['out','retval'], LPFLOAT, 'pfLevel')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'SetMute',
            (['in'], wintypes.BOOL, 'bMute'),
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetMute',
            (['out','retval'], LPBOOL, 'pbMute')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetVolumeStepInfo',
            (['out','retval'], LPUINT, 'pnStep'),
            (['out','retval'], LPUINT, 'pnStepCount')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'VolumeStepUp',
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'VolumeStepDown',
            (['in'], LPCGUID, 'pguidEventContext', None)),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'QueryHardwareSupport',
            (['out','retval'], LPDWORD, 'pdwHardwareSupportMask')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'GetVolumeRange',
            (['out','retval'], LPFLOAT, 'pfLevelMinDB'),
            (['out','retval'], LPFLOAT, 'pfLevelMaxDB'),
            (['out','retval'], LPFLOAT, 'pfVolumeIncrementDB')))
    @classmethod
    def get_default(cls):
        endpoint = IMMDeviceEnumerator.get_default(eRender, eMultimedia)
        interface = endpoint.Activate(cls._iid_, comtypes.CLSCTX_INPROC_SERVER)
        return ctypes.cast(interface, ctypes.POINTER(cls))

#def play_audio(func,file,vol):
ev = IAudioEndpointVolume.get_default()
def ex_vol():
	return int(ev.GetMasterVolumeLevelScalar()*100)
def set_win_vol(lvl):
    ev.SetMasterVolumeLevelScalar(lvl/100)
#func(file,block=True).play()
#ev.SetMasterVolumeLevelScalar(ex_vol)

if os_name == 'nt':
	#from .windows import AudioClip as _PlatformSpecificAudioClip
	from ctypes import windll, c_buffer
	class PlaysoundException(Exception):
		pass

	# TODO: detect errors in all mci calls
	class _PlatformSpecificAudioClip(object):
		def directsend(self, command):
			buf = c_buffer(255)
			command = ''.join(command).encode(getfilesystemencoding())
			errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
			if errorCode:
				errorBuffer = c_buffer(255)
				windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
				exceptionMessage = ('\n	Error ' + str(errorCode) + ' for command:'
									'\n		' + command.decode() +
									'\n	' + errorBuffer.value.decode())
				raise PlaysoundException(exceptionMessage)

			return buf.value

		def __init__(self, filename):
			#filename = filename.replace('/', '\\')
			self.filename = filename
			self._alias = 'mplay_' + str(random.random())

			self.directsend('open "'+filename+'" alias ' +self._alias )
			self.directsend('set %s time format milliseconds' % self._alias)
			
			self._length_ms = int(self.directsend('status %s length' % self._alias).decode())
			#print(self._length_ms)
			#self.directsend('play %s from %d to %d'% (self._alias, 0, self._length_ms) )
		def volume(self, level):
			"""Sets the volume between 0 and 100."""
			assert level >=0 and level <= 100
			self.directsend('setaudio %s volume to %d' %
					(self._alias, level * 10) )

		def isvolume(self):
			return self.directsend('status %s volume' % self._alias) 

		def play(self, start_ms=None, end_ms=None):
			start_ms = 0 if not start_ms else start_ms

			end_ms = self._length_ms if not end_ms else end_ms

			return self.directsend('play %s from %d to %d'
					% (self._alias, start_ms, end_ms) )
		def _mode(self):
			# returns binary
			#print(self.directsend('status %s mode' % self._alias))
			return self.directsend('status %s mode' % self._alias) 
				
		def isrunning(self):
			return self._mode() == b'playing' or self._mode() == b'paused'

		def isplaying(self):
			return self._mode() == b'playing'


		def pause(self):
			self.directsend('pause %s' % self._alias)

		def resume(self):
			self.directsend('resume %s' % self._alias)

		def ispaused(self):
			return self._mode() == b'paused'

		def stop(self):
			self.directsend('stop %s' % self._alias)
			self.directsend('seek %s to start' % self._alias)

		def replay(self):
			self.directsend('stop %s' % self._alias)
			self.play()

		# TODO: this closes the file even if we're still playing.
		# no good.  detect isplaying(), and don't die till then!
		def close(self):
			self.directsend('close %s' % self._alias)
		# def __del__(self):
		# 	self.close()

else:
	raise Exception("mplay4 can't run on your operating system.")


class AudioClip(object):
	__slots__ = ['_clip']

	def __init__(self, filename):
		"""Create an AudioClip for the given filename."""
		self._clip = _PlatformSpecificAudioClip(filename)


	def play(self, start_ms=None, end_ms=None):
		"""
		Start playing the audio clip, and return immediately. Play from
		start_ms to end_ms if either is specified; defaults to beginning
		and end of the clip.  Returns immediately.  If end_ms is specified
		as smaller than start_ms, nothing happens.
		"""

		if end_ms != None and end_ms < start_ms:
			return
		else:
			return self._clip.play(start_ms, end_ms)

	def volume(self, level):
		"""Sets the volume between 0 and 100."""
		assert level >=0 and level <= 100
		return self._clip.volume(level)

	def isplaying(self):
		"""Returns True if the clip is currently playing.  Note that if a
		clip is paused, or if you called play() on a clip and playing has
		completed, this returns False."""
		return self._clip.isplaying()

	def pause(self):
		"""Pause the clip if it is currently playing."""
		return self._clip.pause()

	def resume(self):
		"""Unpause the clip if it is currently paused."""
		return self._clip.resume()

	def replay(self):
		return self._clip.replay()

	def isrunning(self):
		return self._clip.isrunning()

	def ispaused(self):
		"""Returns True if the clip is currently paused."""
		return self._clip.ispaused()

	def stop(self):
		"""Stop the audio clip if it is playing."""
		return self._clip.stop()

	def close(self):
		self._clip.close()

	def seconds(self):
		"""
		Returns the length in seconds of the audio clip, rounded to the
		nearest second.
		"""
		return int(round(float(self.milliseconds()) / 1000))

	def milliseconds(self):
		"""Returns the length in milliseconds of the audio clip."""
		return self._clip._length_ms

	def duration(self):
		return self.seconds()

	def is_volume(self):
		return self._clip.isvolume()

	
def load(filename):
	"""Return an AudioClip for the given filename."""
	return AudioClip(filename)


