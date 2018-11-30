import os

def main():
    files = os.listdir("./")
    for f in files:
        if f.lower()[:] == "rtr.mp4":
            print("processing", f)
            process(f)

def process(f):
    inFile = f
    outFile = f[:-3] + "wav"
   
    cmd = "ffmpeg -i {} -vn  -ac 2 -ar 8000 -ab 148k -f wav {}".format(inFile, outFile)
   
    os.popen(cmd)

main()
    #file_name = os.path.basename(file_path_input)
    #if 'mouthcropped' not in file_name:
    #    raw_file_name = os.path.basename(file_name).split('.')[0]
    #    file_dir = os.path.dirname(file_path_input)
    #    file_path_output = file_dir + '/' + raw_file_name + '.wav'
    #    print('processing file: %s' % file_path_input)
