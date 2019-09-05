import numpy as np 

def load_file(fn, ftype=0, spl=', '):
	print(fn)
	dt = []
	with open(fn) as f:
		for l in f:
			l = l.strip()
			l = l.strip(spl)
			if (ftype == 0):
				#two in one line
				v = l.split(spl)
				if len(v) == 2:
					dt.append(v)

			elif (ftype == 1):
				#one in one line
				dt.append(v)
	
	size = len(dt)
	dt = np.array(dt, np.int32)

	if (ftype == 1):
		dt = np.reshape(dt,(int(size/2),2))

	return dt