
import numpy as np 
import util
#from scipy.signal import lfilter
import fir

coef_fir3 = [ -29, -111, -132, 183, 835, 1002, -508, -3362, -4319, 885, 12875, 25983, 31713,
25983, 12875, 885, -4319, -3362, -508, 1002, 835, 183, -132, -111, -29 ]
coef_fir3 = np.array(coef_fir3, np.int32)
print(len(coef_fir3))

def fir3_simple(dt, coef):
	ss = np.zeros(10, np.complex)

	coef0 = coef[0::3]
	coef1 = coef[2::3]
	coef2 = coef[1::3]

	ss[0] = np.sum(dt[0:9]*coef0)
	ss[1] = np.sum(dt[1:9]*coef1)
	ss[2] = np.sum(dt[1:9]*coef2)
	ss[3] = np.sum(dt[1:10]*coef0)
	ss[4] = np.sum(dt[147:147+8]*coef1)
	ss[5] = np.sum(dt[147:147+8]*coef2)
	ss[6] = np.sum(dt[147:147+9]*coef0)
	ss[7] = np.sum(dt[148:148+8]*coef1)
	ss[8] = np.sum(dt[148:148+8]*coef2)
	ss[9] = np.sum(dt[148:148+9]*coef0)

	return np.around(ss / 2**15)


def fir3_opt(dt, coef):
	res = []
	n = len(dt)

	
	cl = len(coef)
	dtx = np.append(np.zeros(cl//3, np.complex), dt)

	coef0 = coef[0::3]
	coef1 = coef[2::3]
	coef2 = coef[1::3]

	for i in range(0, n):
		s = np.sum(dtx[i  :i+9] * coef0)
		res.append(s)

		s = np.sum(dtx[i+1:i+9] * coef1)
		res.append(s)

		s = np.sum(dtx[i+1:i+9] * coef2)
		res.append(s)
		
	res = np.array(res, np.complex) / 2**15

	return res


if __name__ == '__main__':
	fn = "fir_up3.inp"

	dt_in = util.load_complex(fn,",\t")
	
	#dt_in = dt_in / 2
	#dt_in = np.around(dt_in)

	#fir3_simple(dt_in, coef_fir3)

	print(len(dt_in))

	# optimization - no need to upsample, less mempry, less multiplications
	dd2 = fir3_opt(dt_in, coef_fir3)
	dd2 = np.around(dd2)
	#print(dd2[0:50])

	
	util.write_complex(dd2, "fir_up3.out")
	
	# comparing to scypy FIR function
	# upsemple by 3
	l = 3 * len(dt_in)
	dt_up = np.zeros(l, np.complex)
	dt_up[::3] = dt_in
	#dt_ref = lfilter(coef_fir3, 1.0, dt_up) / 2**15
	#dt_ref = fir.fir_s(dt_up, coef_fir3, 15) 
	dt_ref = fir.fir(dt_up, coef_fir3, 15) 
	dt_ref = np.around(dt_ref)

	print("Compare to scipy FIR")
	diff = dd2 - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 0]
	print(f"Values count with difference: {len(diff)}")

	dd2 = np.append(np.zeros(64, np.complex), dd2)
	# comparing to ref file
	fn_ref = "fir_up3.ref"
	dt_ref = util.load_complex(fn_ref, ", ")
	##print(dt_ref[6200:])
	
	print("Compare to REF")
	diff = dd2 - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 1.5]
	#print(diff)
	print(f"Values count with difference more than 1 + 1j: {len(diff)}")

	#Saturation problems in REF can be seen