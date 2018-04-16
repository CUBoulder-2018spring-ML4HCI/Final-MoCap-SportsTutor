import numpy as np
import argparse

from dtw import dtw
from threading import Thread
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc import osc_bundle_builder

from sklearn.metrics.pairwise import euclidean_distances as euclidean

_test_samples = [[[1,2,3],[1,2,3],[4,5,6],[3,4,5]],
                 [[1,2,3],[1,2,3],[4,6,6],[3,4,6]],
                 [[1,1,3],[1,2,3],[4,5,5],[6,4,5]]]

_test_test = [[1,1,3],[1,2,3],[4,5,6],[5,4,5]]


training_samples = []
Y = []

temp_holder = []
END_SAMPLE = False

""" Make cmd run the processing script to stream data to stdout"""
def get_data_gen(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        print line
        if line == '' and p.poll() != None:
            break
        yield ''.join(stdout)


def stop(*args):
    END_SAMPLE = True
    if (not training_samples):
        temp_holder_copy = list(temp_holder)
        training_samples.append(temp_holder_copy)
        temp_holder.clear()
    if not (Y == []):
        dtws = []
        for x in training_samples:
            # Perform DTW on each training sample, finding min
            distance = dtw(x, Y, euclidean)
            dtws.append(distance)

        min_dist = min(dtws)
        print ("MINIMUM DISTANCE: ", min_dist)
    print (training_samples)

def start(*args):
    END_SAMPLE = False

# Get training data via OSC and put into global matrix
def get_train_data(*args):
    x = args[1:]
    temp_holder.append(list(x))

# Get testing data and perform DTW w/ respect to training
def test(*args):
    Y.append(list(args[1:]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port", type=int, default=6448, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/train", get_train_data)
    dispatcher.map("/test", test)
    dispatcher.map("/stop", stop)
    dispatcher.map("/start", start)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
