from threading import Thread
from tkinter import *
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc import osc_bundle_builder

training = True

running = False
root = Tk()
root.geometry("600x500")

client = udp_client.SimpleUDPClient("127.0.0.1", 8000)

def send_osc(event):
    global running
    print("sending...")
    running = True

def stop_osc(event):
    global running
    running = False
    print("stopping...")

def send():
    while True: # Thread will run infinitely in the background
        if running:
            print("send")

def set_train(event):
    global training
    training = True

def set_test(event):
    global training
    training = False

def handle_data(*args):
    return


dispatcher = dispatcher.Dispatcher()
dispatcher.map("/data", handle_data)


server = osc_server.ThreadingOSCUDPServer(('127.0.0.1', 6448), dispatcher)
print("Serving on {}".format(server.server_address))

train_button= Button(root, text = "Training Mode")
train_button.pack(side=RIGHT)
train_button.bind('<ButtonPress-1>', set_train)

test_button = Button(root, text = "Testing Mode")
test_button.pack(side=RIGHT)
test_button.bind('<ButtonPress-1>', set_test)

button = Button(root, text ="Record")
button.pack(side=LEFT)
button.bind('<ButtonPress-1>',send_osc)
button.bind('<ButtonRelease-1>',stop_osc)
# lbl = Label(window, text="Hello")

# Create and start the new thread
t = Thread(target = send, args = ())
t.start()

root.mainloop()
server.serve_forever()
