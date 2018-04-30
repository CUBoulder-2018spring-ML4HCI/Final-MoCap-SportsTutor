from dtw import dtw
from threading import Thread
import numpy
from sklearn.metrics.pairwise import euclidean_distances as euclidean

training_samples = []
testing_samples = []

temp_holder = []
GET_SAMPLE_TRAIN = False
GET_SAMPLE_TEST = False
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

PIPE = open("/tmp/un_pipe", 'r')

def stop_train():
	global GET_SAMPLE_TRAIN
	GET_SAMPLE_TRAIN = False

def stop_test():
	global GET_SAMPLE_TEST
	GET_SAMPLE_TEST = False
	best_shot = get_best_shot()
	worst_joint = get_largest_distance()

def get_train_data():
	global GET_SAMPLE_TRAIN
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
			global testing_samples
			xx = read_pipe()
			if xx:
				testing_samples.append(xx)

def poll_train():
	global GET_SAMPLE_TRAIN
	while True:
		if GET_SAMPLE_TRAIN:
			global temp_holder
			xx = read_pipe()
			if xx:
				temp_holder.append(xx)

def get_largest_distance():
	global training_samples
	global testing_samples
	global skeletal_index

	#Builds a 2D array containing 24 smaller arrays. Each smaller arrary holds all data points
	#taken for that specific joint during training.
	datapoints_compilation = [[]] * len(training_samples[0])
	for sample in range(0, len(training_samples)):
		for point in range(0, len(sample)):
			datapoints_compilation[point].append(training_samples[sample][point])
	
	#Goes through each point array and calculates the average and standard deviation,
	#leaving training_summary as a 24-item array with ditionaries for each item
	training_summary = []
	for datapoint_arr in datapoints_compilation:
		training_summary.append({"average":(sum(datapoint_arr) / len(datapoint_arr)), 
								 "stdev":numpy.std(numpy.array(datapoint_arr))
								})

	#Builds a 2D array containing 24 smaller arrays. Each smaller arrary holds all data points
	#taken for that specific joint during testing.
	datapoints_compilation = [[]] * len(testing_samples[0])
	for sample in range(0, len(testing_samples)):
		for point in range(0, len(sample)):
			datapoints_compilation[point].append(testing_samples[sample][point])

	#Goes through each point array and calculates the average,
	#leaving testing_summary as a 24-item array with ditionaries for each item
	testing_summary = []
	for datapoint_arr in datapoints_compilation:
		testing_summary.append({"average":(sum(datapoint_arr) / len(datapoint_arr))})
	
	#Goes through once and tries to find the largest average outside of a standard deviation.
	#If none exist outside of a standard deviation, just find the largest distance
	curr_max = 0
	for x in range(0, len(testing_summary)):
		if (abs(testing_summary[x]["average"] - training_summary[x]["average"]) > curr_max) \
			and ((testing_summary[x]["average"] > training_summary[x]["average"] + training_summary[x]["stdev"]) \
			or (testing_summary[x])["average"] < training_summary[x]["average"] - training_summary[x]["stdev"]):
				curr_max = x
	if curr_max == 0:
		for y in range(0, len(testing_summary)):
			if (abs(testing_summary[x]["average"] - training_summary[x]["average"]) > curr_max):
				curr_max = y
	
	#Correlates greatest distance with joint
	if curr_max < 24:
		return skeletal_index[curr_max]
	else:
		return 0

def get_best_shot():
	global training_samples
	global testing_samples

	dtws = []
	for x in training_samples:
		distance = dtw(x, testing_samples, euclidean)
		dtws.append(distance)
	return min(dtws)
	

#NOTE: DO WE NEED THIS
"""
def stop():
	global temp_holder
	global training_samples
	global testing_samples
	if (testing_samples == []):
		temp_holder_copy = list(temp_holder)
		training_samples.append(temp_holder_copy)
		temp_holder.clear()
	else:
		dtws = []
		for x in training_samples:
			distance = dtw(x, testing_samples, euclidean)
			dtws.append(distance)
		best_shot = min(dtws)
	return best_shot
"""

train_thread = Thread(target = poll_train, args = ())
test_thread = Thread(target = poll_test, args = ())

train_thread.start()
test_thread.start()

