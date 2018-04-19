import subprocess


with open("/var/folders/8h/1wdq8kx52lx_gfd96zxqg4dc0000gn/T/tmp.RtlmKwpP/pipe", 'rb') as pipe:
    while True:
        line = pipe.read()
        if not(len(line) == 0):
            print (line)



""" Make cmd run the processing script to stream data to stdout"""
def get_data_gen(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        #print line
        if line == '' and p.poll() != None:
            break
        yield ''.join(stdout)
