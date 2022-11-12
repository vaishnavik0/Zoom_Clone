from vidstream import *
import tkinter as tk
import socket
import threading 
import requests

# getting our private IP address using socket module
local_ip_address = socket.gethostbyname(socket.gethostname())

# when it comes to listening and receiving we want to have just one instance and one server for video connections 
# 1 listener or receiver for audio connections

server = StreamingServer(local_ip_address, 7777)

receiver = AudioReceiver(local_ip_address, 6666)


# In Total 4 functions 
# 1. Starts listening for incoming connections
# 2. Starts an outgoing camera stream
# 3. Starts screen sharing to another client 
# 4. Starts audio stream

# function : 1 
def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=reciver.start_server)
    t1.start()
    t2.start()

# function : 2
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()


def start_screen_sharing():
    screen_clinet = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 9999)
    t4 = threading.Thread(target=screen_clinet.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 8888)
    t5 = threading.Thread(target=screen_sender.start_stream)
    t5.start()
# public_ip_address = requests.get('https://api.ipify.org')


# GUI

window = tk.Tk()
window.title("VK Zoom Clone")
window.geometry('300x200')


lable_target_ip = tk.Label(window, text ="Target IP:")
lable_target_ip.pack()


text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

# buttons

btn_listen = tk.Button(window, text="Start Listening" , width=50, command= start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream" , width=50, command = start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing" , width=50, command = start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream" , width=50, command = start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()

