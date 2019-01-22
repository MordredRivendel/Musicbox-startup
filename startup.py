from mpd import MPDClient
import sys

# Mount Net-Drive to mopidy

# set NetworkPath
npath = '//IP_ADDRESSE_FREIGABE/FREIGABENAME'
# set LocalPath
lpath = '/mnt/smb/'
# set User
username = ''
# set Password
password = ''

if path != '':
	os.system ("mount -t cifs -o user=" + username + ",password=" + password + ",rw,file_mode=0777,dir_mode=0777 " +  npath + " " + lpath


		   

		   
# Startup Volume
# set Startup Volume
startvolume = '' # 1 - 100
		   
if startupvolume != '':
	client = connectMPD()
	client.setvol(startvolume)
	client.close()	
		   
		   
		   
# Autostart File  after boot

# set Autostart File
autostart = 'file:///var/lib/mopidy/network/start.mp3'

if autostart != '':
	client = connectMPD()
	client.stop()
	client.clear()
	client.add(autostart)
	client.play()
	client.close()
