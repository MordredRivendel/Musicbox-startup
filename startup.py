from mpd import MPDClient
import sys

autostart = 'file:///var/lib/mopidy/network/start.mp3'    # autostart funktion
if autostart != '':
	client = connectMPD()
	client.stop()
	client.clear()
	client.add(autostart)
	client.play()
client.close()
