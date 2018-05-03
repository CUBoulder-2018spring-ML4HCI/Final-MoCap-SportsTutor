from dtw import dtw
import threading
from threading import Thread
from multiprocessing import Process, Queue
import numpy as np
import random
import mutex
import sys
from sklearn.metrics.pairwise import euclidean_distances as euclidean


boolean_lock = threading.Lock()

training_samples = []
testing_samples = []
temp_holder = []

prev_get_data = False
prev_which_data = 'train'

q = Queue()
data_q = Queue()
test_q = Queue()

# GET_SAMPLE_TRAIN = False
# GET_SAMPLE_TEST = False


GET_DATA = False
WHICH_DATA = 'train'
skeletal_index = {
	0:"LEFT WRIST X-AXIS",
	1:"LEFT WRIST Y-AXIS",
	2:"LEFT WRIST Z-AXIS",
	3:"RIGHT WRIST X-AXIS",
	4:"RIGHT WRIST Y-AXIS",
	5:"RIGHT WRIST Z-AXIS",
	6:"LEFT SHOULDER X-AXIS",
	7:"LEFT SHOULDER Y-AXIS",
	8:"LEFT SHOULDER Z-AXIS",
	9:"RIGHT SHOULDER X-AXIS",
	10:"RIGHT SHOULDER Y-AXIS",
	11:"RIGHT SHOULDER Z-AXIS",
	12:"LEFT ELBOW X-AXIS",
	13:"LEFT ELBOW Y-AXIS",
	14:"LEFT ELBOW Z-AXIS",
	15:"RIGHT ELBOW X-AXIS",
	16:"RIGHT ELBOW Y-AXIS",
	17:"RIGHT ELBOW Z-AXIS",
	18:"MICROBIT 1 X-AXIS",
	19:"MICROBIT 1 Y-AXIS",
	20:"MICROBIT 1 Z-AXIS",
	21:"MICROBIT 2 X-AXIS",
	22:"MICROBIT 2 Y-AXIS",
	23:"MICROBIT 2 Z-AXIS"
}

#PIPE = open("/tmp/un_pipe", 'r')

"""
Setter to ensure a more thread safe context
Only one thread at a time can set GET_DATA and WHICH_DATA
"""
def set_get_data(b):
	global prev_which_data
	print ("sending data to queue: ", (b, prev_which_data))
	q.put((b, prev_which_data))
	prev_get_data = b

def set_which_data(s):
	global prev_get_data
	print ("sending data to queue: ", (prev_get_data, s))
	q.put((prev_get_data, s))
	prev_which_data = s

def set_both(t):
	q.put(t)

def stop_train():
	stop()
	set_get_data(False)


def stop_test():
	global testing_samples
	set_get_data(False)
	stop()
	#GET_DATA = Fals
	#best_shot = get_best_shot()
	#worst_joint = get_largest_distance()

def get_train_data():
	set_both((True, 'train'))

def get_test_data():
	set_both((True, 'test'))

def read_pipe(PIPE):
	#global PIPE
	line = PIPE.readline()
	print "line: " + line
	if not(len(line) == 0):
		line_arr = line.split(",")
		line_arr = line_arr[:len(line_arr)-1]
		xx = [int(float(x)) for x in line_arr if not(x == '')]
		return xx
	else:
		return None

"""
The threaded function
Constantly checks whether or not GET_DATA is true
if it is true, figure out which array to put data into via a boolean

Only 1 file descriptor, created in the only thread that reads from it

Only shared access memory is the boolean
"""
def poll(q):
	# global GET_DATA
	# global WHICH_DATA
	print("pre pipe")
	PIPE = open("/tmp/un_pipe", 'r')
	print("post pipe")
	get_data = False
	which_data = 'train'
	while True:
		try:
			q_tuple = q.get(False)
			get_data = q_tuple[0]
			which_data = q_tuple[1]
			print ("got data from queue: ", (get_data, which_data))
		except:
			continue
		if get_data:
			global testing_samples
			global training_samples
			if which_data == 'train':
				xx = read_pipe(PIPE)
				if xx:
					print "getting train"
					data_q.put(list(xx))
					#temp_holder.append(xx)
			else:
				# it does not get to this block
				xx = read_pipe(PIPE)
				if xx:
					print "getting test"
					#testing_samples.append(xx)
					test_q.put(list(xx))


# def poll_test():
# 	global GET_SAMPLE_TEST
# 	while True:
# 		if GET_SAMPLE_TEST:
# 			global testing_samples
# 			xx = read_pipe()
# 			if xx:
# 				testing_samples.append(xx)
#
# def poll_train():
# 	global GET_SAMPLE_TRAIN
# 	while True:
# 		if GET_SAMPLE_TRAIN:
# 			global temp_holder
# 			xx = read_pipe()
# 			if xx:
# 				temp_holder.append(xx)

def get_largest_distance():
	try:
		global training_samples
		global testing_samples
		global skeletal_index
		#print training_samples

		# training_samples[rows, sample, column/joint]
		# print training_samples
		# training_samples = np.array(training_samples)
		# print type(training_samples)
		# print training_samples
		# testing_samples = np.array(testing_samples)
		# print testing_samples.shape
		# all_dtws = []
		# for joint in range(0, len(training_samples[0][0])):
		# 	joint_dtws = []
		# 	for sample, _ in enumerate(training_samples):
		# 		joint_train = training_samples[:,sample, joint]
		# 		joint_test = testing_samples[:, joint]
		# 		joint_dtws.append(dtw(joint_train, joint_test, euclidean)[0])
		#
		# 	all_dtws.append(min(joint_dtws))
		#
		# print max(all_dtws)


		all_dtws = []
		print "looping through joint"
		print training_samples
		for joint in range(0, len(training_samples[0][0])):
			joint_dtws = []
			for sample in training_samples:
				print "looping through training_samples"
				joint_train = np.array(sample)[:,joint]
				joint_test = np.array(testing_samples)[:, joint]
				print "created arrays"
				joint_dtws.append(dtw(joint_train, joint_test, euclidean)[0])

			all_dtws.append(min(joint_dtws))

		curr_max = all_dtws.index(max(all_dtws))

		# #datapoints_compilation is a 2d array consiting of every point in the 24 points
		# # as a row. For example, every x-dimension of your left wrist is a row
		#
		# print("Building datapoints compilation for training samples")
		# datapoints_compilation = []
		# training_samples = np.array(training_samples)
		# for i in range(0, len(training_samples[0][0])):
		# 	datapoints_compilation.append(training_samples[:,:,i].flatten())
		#
		# # go through each testing, and each row of the datapoints
		# #compute z-score, and find highest z-score
		# #that is what you must change


		#curr_max = 12
		#Correlates greatest distance with joint
		if curr_max < 24:
			return skeletal_index[curr_max]
		else:
			return skeletal_index[0]
	except Exception as e:
		print(e.__str__())
		return skeletal_index[random.randint(0,23)]

def get_best_shot():
	global training_samples
	global testing_samples

	dtws = []
	for x in training_samples:
		distance = dtw(x, testing_samples, euclidean)
		dtws.append(distance)
	return min(dtws)



def stop():
	global training_samples
	global testing_samples

	best_shot = None
	temp_holder = []
	if (test_q.empty()):
		while not(data_q.empty()):
			temp_holder.append(list(data_q.get()))
		training_samples.append(temp_holder)
		#print training_samples
	else:
		print ("Above test for test being empty")
		while not(test_q.empty()):
			print ("Looping through shared test queue")
			testing_samples.append(list(test_q.get()))
	# 	for x in training_samples:
	# 		distance = dtw(x, testing_samples, euclidean)
	# 		dtws.append(distance)
	# 	best_shot = min(dtws)
	# if (best_shot):
	# 	print best_shot
	return


# polling_thread = Thread(target = poll, args = ())
# polling_thread.start()
p = Process(target = poll, args = (q,))
p.start()
