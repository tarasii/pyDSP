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

def load_complex(fn, spl=', '):
	dt = load_file(fn, 0, spl)
	dt = [x + y*1j for x, y in dt]
	dt = np.array(dt, np.complex)
	return dt

def load_complex_numpy(fn, spl=', '):
	dt = np.genfromtxt(fn, delimiter=spl) 
	dt = np.delete(dt,range(2, sh[1]),1)
	dt = dt.view(complex).reshape(-1)
	sh = np.shape(dt)

	#array_real, array_imag = np.loadtxt(fn, unpack=True, delimiter=spl)
	#dt = array_real + 1j * array_imag
	return dt

def write_complex(dt, fn, spl=', '):
	#np.savetxt(fn, np.column_stack([dt.real, dt.imag]))
	dtx = dt.view(float).reshape(-1, 2)
	np.savetxt(fn, dtx, delimiter=spl, fmt='%6.0f')

if __name__ == '__main__':
	fn = "fir_up3.inp"
	dt = load_complex(fn, spl=',\t')
	fn = "fir_up3.ref"
	dt = load_complex(fn, spl=', ')	
	print(dt)