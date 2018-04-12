import numpy as np
from dtw import dtw

X = []
Y = []

# Get training data via OSC and put into global matrix
def get_train_data(*args):
    return

# Get testing data and perform DTW w/ respect to training
def get_test_data(*args):
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port", type=int, default=6449, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/train", get_train_data)
    dispatcher.map("/test", get_test_data)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
