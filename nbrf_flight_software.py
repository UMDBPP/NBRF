import os
import time

serial_num = '0000000000000000f77c60dc249856c3'
a = '0'
f = '900:930'
p = '0'
l = '0'
g = '0'
w = '2445'
N = '120'

data_dir = './ns114_samples/'

def main():
	while(1):
		curr_time = int(time.time())
		filename = f'{data_dir}{curr_time}.bin'
		os.system(f"hackrf_sweep -d {serial_num} -a {a} -f {f} -p {p} -l {l} -g {g} -w {w} -N {N} -B -r {filename}")
		#os.system('hackrf_sweep -d 0000000000000000f77c60dc249856c3 -a 0 -f 900:930 -p 0 -l 0 -g 0 -w 2445 -N 120 -B -r test.bin')
		time.sleep(1)
	

if __name__ == '__main__':
	main()
