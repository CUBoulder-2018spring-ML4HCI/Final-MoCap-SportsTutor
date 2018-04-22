from dtw import dtw
from sklearn.metrics.pairwise import euclidean_distances as euclidean

training_samples = []
Y = []

temp_holder = []
END_SAMPLE = False

PIPE = open("/tmp/un_pipe", 'r')

def read_pipe():
	global PIPE
	line = PIPE.read()
	if not(len(line) == 0):
		line_arr = line.split(",")
		xx = [x for x in line_arr]
		return xx
	else:
		return None

def get_test_data():
	global Y
	xx = read_pipe()
	if xx:
		Y.append(xx)

def get_training_data():
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

	print (training_samples)
