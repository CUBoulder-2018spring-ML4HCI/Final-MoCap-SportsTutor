with open("/var/folders/8h/1wdq8kx52lx_gfd96zxqg4dc0000gn/T/tmp.RtlmKwpP/pipe", 'rb') as pipe:
    while True:
        line = pipe.read()
        if not(len(line) == 0):
            print (line)