import numpy as np 
import util
from scipy.signal import lfilter
import fir

fir_up2_coef = [      
	   10,	    0,    -30,     0,    68,     0,  -136,
	    0,	  244,      0,  -408,     0,   652,     0,
	-1008,	    0,   1526,     0, -2322,     0,  3676,
	    0,  -6646,      0, 20756, 32767, 20756,     0,
	-6646,      0,   3676,     0, -2322,     0,  1526,
	    0,  -1008,      0,   652,     0,  -408,     0,
	  244,      0,   -136,     0,    68,     0,   -30,
	    0,     10 
]



def fir_up2_opt(dt, coef):
	""" optimized FIR function """

	res = []

	cl = len(coef)
	dtx = np.append(np.zeros(cl//2, np.complex), dt)
	coef_odd = coef[::2]
	
	l_center = len(coef)//2
	coef_center = coef[l_center]

	n = len(dt)
	for i in range(0, n):
		s = np.sum(dtx[i:i+len(coef_odd)]*coef_odd)
		res.append(s)
		s = dtx[i+l_center//2+1]*coef_center
		res.append(s)

	res = np.array(res, np.complex) / 2**15

	return res


if __name__ == '__main__':
	fn_inp = "fir_up2.inp"

	dt_in = util.load_complex(fn_inp, ", ")
	l = 2*len(dt_in)

	# upsemple by 2
	dt_up = np.zeros(l, np.complex)
	dt_up[::2] = dt_in
	out = fir.fir(dt_up, np.array(fir_up2_coef, np.complex), 15);
	out = np.around(out)

	# comparing to ref file
	fn_ref = "fir_up2.ref"
	dt_ref = util.load_complex(fn_ref, ", ")
	diff = out - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 1.5]
	print(f"Values count with difference more than 1 + 1j: {len(diff)}")

	# comparing to scypy FIR function
	dt_ref = lfilter(fir_up2_coef, 1.0, dt_up) / 2**15
	dt_ref = np.around(dt_ref)

	diff = out - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 0]
	print(f"Values count with difference: {len(diff)}")

	# optimization - no need to upsample, less mempry, less multiplications
	out2 = fir_up2_opt(dt_in, fir_up2_coef);
	out2 = np.around(out2)

	diff = out2 - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 0]
	print(f"Values count with difference: {len(diff)}")

