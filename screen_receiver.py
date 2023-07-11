from vidstream import AudioReceiver,AudioSender
from vidstream import StreamingServer

import threading
import time

receiving =StreamingServer('192.168.40.137',9997)


t1=threading.Thread(target=receiving.start_server)
t1.start()


while input("")!= "STOP":
    continue

receiving.stop_server()
