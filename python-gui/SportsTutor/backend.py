from dtw import dtw
from threading import Thread
from sklearn.metrics.pairwise import euclidean_distances as euclidean

training_samples = []
Y = []

temp_holder = []
GET_SAMPLE_TRAIN = False
GET_SAMPLE_TEST = False

# PIPE = open("/tmp/un_pipe", 'r')



def stop_train():
	global GET_SAMPLE_TRAIN
	GET_SAMPLE_TRAIN = False

def stop_test():
	global GET_SAMPLE_TEST
	GET_SAMPLE_TEST = False

def get_train_data():
	global GET_SAMPLE_TRAIN
	# print ("GETTING TRAINING DATA HO")
	GET_SAMPLE_TRAIN = True

def get_test_data():
	global GET_SAMPLE_TEST
	GET_SAMPLE_TEST = True

def read_pipe():
	global PIPE
	line = PIPE.readline()
	if not(len(line) == 0):
		line_arr = line.split(",")
		line_arr = line_arr[:len(line_arr)-1]
		print (len(line_arr))
		xx = [float(x) for x in line_arr if not(x == '')]
		return xx
	else:
		return None

def poll_test():
	global GET_SAMPLE_TEST
	while True:
		if GET_SAMPLE_TEST:
			global Y
			xx = read_pipe()
			if xx:
				Y.append(xx)

def poll_train():
	global GET_SAMPLE_TRAIn
	# print ("we in this bitch")
	while True:
		if GET_SAMPLE_TRAIN:
			# print ("WE DOUBLE IN THIE BITCH")
			global temp_holder
			xx = read_pipe()
			if xx:
				temp_holder.append(xx)


def stop():
	global temp_holder
	global training_samples
	global Y
	if (Y == []):
		temp_holder_copy = list(temp_holder)
		training_samples.append(temp_holder_copy)
		temp_holder.clear()
	else:
		dtws = []
		for x in training_samples:
			distance = dtw(x, Y, euclidean)
			dtws.append(distance)
		min_dist = min(dtws)
		print ("MIN DISTANCE: ", mind_dist)


train_thread = Thread(target = poll_train, args = ())
test_thread = Thread(target = poll_test, args = ())

train_thread.start()
test_thread.start()

