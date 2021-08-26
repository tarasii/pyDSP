
import numpy as np 
import util
from scipy.signal import lfilter

coef_up2_down3_full = [ 2, -47, -126, -247, -381, -472, -438, -193, 322, 1111, 2108, 3176, 4133, 4798, 5036 , \
4798, 4133, 3176, 2108, 1111, 322, -193, -438, -472, -381, -247, -126, -47, 2 ]

coef_up2_down3 = [ 2, -47, -126, -247, -381, -472, -438, -193, 322, 1111, 2108, 3176, 4133, 4798, 5036 ]
coef_up2_down3 = np.array(coef_up2_down3, np.int32)
#print(len(coef_up2_down3))

def fir23_simple(dt):
	ss = np.zeros(18, np.complex)

	ss[0] = np.sum(dt[0:1]*np.take(coef_up2_down3,[ 0 ]))
	#zz = np.sum(dt[0:1]*np.take(coef_up2_down3,[ 1 ]))
	#zz = np.sum(dt[0:2]*np.take(coef_up2_down3,[ 2, 0 ]))
	ss[1] = np.sum(dt[0:2]*np.take(coef_up2_down3,[ 3, 1 ]))
	#zz = np.sum(dt[0:3]*np.take(coef_up2_down3,[ 4, 2, 0 ]))
	#zz = np.sum(dt[0:3]*np.take(coef_up2_down3,[ 5, 3, 1 ]))
	ss[2] = np.sum(dt[0:4]*np.take(coef_up2_down3,[ 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:4]*np.take(coef_up2_down3,[ 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:5]*np.take(coef_up2_down3,[ 8, 6, 4, 2, 0 ]))
	ss[3] = np.sum(dt[0:5]*np.take(coef_up2_down3,[ 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:6]*np.take(coef_up2_down3,[ 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:6]*np.take(coef_up2_down3,[ 11, 9, 7, 5, 3, 1 ]))
	ss[4] = np.sum(dt[0:7]*np.take(coef_up2_down3,[ 12, 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:7]*np.take(coef_up2_down3,[ 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:8]*np.take(coef_up2_down3,[ 14, 12, 10, 8, 6, 4, 2, 0 ]))
	ss[5] = np.sum(dt[0:8]*np.take(coef_up2_down3,[ 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:9]*np.take(coef_up2_down3,[ 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:9]*np.take(coef_up2_down3,[ 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	ss[6] = np.sum(dt[0:10]*np.take(coef_up2_down3,[ 10, 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:10]*np.take(coef_up2_down3,[ 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:11]*np.take(coef_up2_down3,[ 8, 10, 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	ss[7] = np.sum(dt[0:11]*np.take(coef_up2_down3,[ 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:12]*np.take(coef_up2_down3,[ 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:12]*np.take(coef_up2_down3,[ 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	ss[8] = np.sum(dt[0:13]*np.take(coef_up2_down3,[ 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[0:13]*np.take(coef_up2_down3,[ 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:14]*np.take(coef_up2_down3,[ 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	##first fool
	ss[9] = np.sum(dt[0:14]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[0:15]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2, 0 ]))
	#zz = np.sum(dt[1:15]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	ss[10] = np.sum(dt[1:16]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[2:16]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[2:17]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	ss[11] = np.sum(dt[3:17]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[3:18]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[4:18]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	ss[12] = np.sum(dt[4:19]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[5:19]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[5:20]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	ss[13] = np.sum(dt[6:20]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[6:21]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[7:21]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	ss[14] = np.sum(dt[7:22]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[8:22]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[8:23]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	ss[15] = np.sum(dt[9:23]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[9:24]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[10:24]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	ss[16] = np.sum(dt[10:25]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	#zz = np.sum(dt[11:25]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[11:26]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))
	ss[17] = np.sum(dt[12:26]*np.take(coef_up2_down3,[ 1, 3, 5, 7, 9, 11, 13, 13, 11, 9, 7, 5, 3, 1 ]))
	#zz = np.sum(dt[12:27]*np.take(coef_up2_down3,[ 0, 2, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6, 4, 2 ,0]))

	return np.around(ss / 2**15)


def fir_up2_down3_loop(dt):
	ss = np.zeros(8, np.complex)

	for i in range(0, 7):
		s = np.take(dt,[ 0+i,  2+i,  3+i,  5+i,  6+i,  8+i,  9+i, 11+i]) \
		  + np.take(dt,[14-i, 15-i, 17-i, 18-i, 20-i, 21-i, 23-i, 24-i])
		cc = np.array([coef_up2_down3[2*i], coef_up2_down3[2*i+1]]*4, np.int32)
		ss = ss + s * cc

	s = np.take(dt, [ 7,  9, 10, 12, 13, 15, 16, 18]) 
	cc = np.array([coef_up2_down3[14],0]*4, np.int32)
	ss = ss + s * cc
	ss = ss / 2**15
	return ss

def fir_up2_down3(dt):
	l = len(dt)

	dt = np.insert(dt, 0, np.zeros(14, np.complex))

	res = np.zeros(round(l/12*8), np.complex)
	for x in range(0, round(l/12)):
		z = fir_up2_down3_loop(dt[x*12: x*12+25])
		res[x*8: x*8+8] = z
	return np.around(res)

if __name__ == '__main__':
	fn = "fir_up2_down3.inp"

	dt_in = util.load_complex(fn)
	dt_in = np.around(dt_in/2)

	#print(fir23_simple(dt_in))

	out2 = fir_up2_down3(dt_in)

	# comparing to ref file
	fn_ref = "fir_up2_down3.ref"
	dt_ref = util.load_complex(fn_ref, ", ")

	print("Compare to REF")
	diff = out2 - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 1.5]
	print(f"Values count with difference more than 1 + 1j: {len(diff)}")	
	#util.write_complex(out2, "fir_up2_down3.out")


	# comparing to scypy FIR function
	# upsemple by 2
	l = 2 * len(dt_in)
	dt_up = np.zeros(l, np.complex)
	dt_up[::2] = dt_in
	dt_ref = lfilter(coef_up2_down3_full, 1.0, dt_up) / 2**15
	dt_ref = np.around(dt_ref[::3])

	print("Compare to scipy FIR")
	diff = out2 - dt_ref
	diff = np.absolute(diff)
	diff = diff[diff > 0]
	print(f"Values count with difference: {len(diff)}")
	#util.write_complex(dt_ref, "fir_up2_down3.out")

