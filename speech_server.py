import socket
import speech_recognition as sr
import time
import os

TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

r = sr.Recognizer()
m = sr.Microphone()
time.sleep(2)

print ('Connection address:', addr)
while 1:
	data = conn.recv(BUFFER_SIZE)

 	if not data:
        	print ("no request")
        	continue
	import speech_recognition as sr
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print ("Please wait. Calibrating microphone...")
		r.adjust_for_ambient_noise(source, duration=5)
		print ("Say something!")
		audio = r.listen(source)


	try:

		print ("Speech Recognition thinks you said " + r.recognize_google(audio))
		conn.send(r.recognize_google(audio))
	except sr.UnknownValueError:
		print ("Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print ("Could not request results from Speech Recognition service; {0}".format(e))






conn.close()

