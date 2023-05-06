import NBRF
import time

def main():
	radio = NBRF.NBRF()
	while(1):
		try:
			curr_time = int(time.time())
			
			radio.set_filename(f'./ns114_samples/{curr_time}.bin')
			radio.start()
			time.sleep(1)
			radio.stop()
			radio.wait()
			time.sleep(20)
		except:
			radio.stop()
			radio.wait()
			pass


if __name__ == '__main__':
	main()
