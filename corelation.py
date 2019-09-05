import numpy as np 
import util

def corr_left(A, B, n, m):
	tmp = np.zeros(n, np.complex)
	res = tmp;

	tmp[0:n] = A[0:n]
	for i in range(1, n+1):
		res = res + tmp * np.conj(B[n-i])
		tmp = np.roll(tmp, 1)
		tmp[0] = 0

	return res

def corr_right(A, B, n, m):
	tmp = np.zeros(n, np.complex)
	res = tmp;

	tmp[0:n] = A[0:n]
	for i in range(0, n):
		res = res + tmp * np.conj(B[i])
		tmp = np.roll(tmp, -1)
		tmp[n-1] = 0

	return res

def xcorr(A, B, n, m):
	tmp = np.zeros(n, np.complex)
	res = np.zeros(2*m - 1 , np.complex)
	mpy = tmp;

	mpy = corr_left(A, B, n, m)
	res[0:m] = mpy[n-m:n]

	mpy = corr_right(A, B, n, m)
	res[m:] = mpy[1:m]

	return res

def auto_corr(A, n, m):
	res = xcorr(A, A, n, m)
	return res

def auto_corr_opt(A, n, m):
	""" auto_corr_opt will take less cycles than auto_corr"""
	tmp = np.zeros(n, np.complex)
	res = np.zeros(2*m - 1 , np.complex)
	mpy = tmp;

	mpy = corr_right(A, A, n, m)
	res[m:] = mpy[1:m]

	mpy = np.conj(mpy)
	mpy = np.flip(mpy,0)
	res[0:m] = mpy[n-m:n]

	return res


def tester_xcorr(dt, n, m):

	A = dt_in[0:n]
	B = dt_in[n:2*n]

	res = xcorr(A, B, n, m)	
	print(res)

	res = np.correlate(A, B,"full")
	if (n == m): 
		print(res)
	else:
		print(res[n-m:m-n])

def tester_acorr(dt, n, m):

	A = dt_in[0:n]

	res = auto_corr_opt(A, n, m)	
	print(res)

	res = np.correlate(A, A,"full")
	if (n == m): 
		print(res)
	else:
		print(res[n-m:m-n])

if __name__ == '__main__':
	fn = "crosscorr.in"
	dt_in = util.load_file(fn)	
	dt_in = [x + y*1j for x, y in dt_in]

	#tester_xcorr(dt_in, 5, 3)
	#tester_xcorr(dt_in, 16, 16)
	#tester_xcorr(dt_in, 32, 32)
	#tester_xcorr(dt_in, 32, 16)
	#tester_xcorr(dt_in, 39, 25)
	tester_acorr(dt_in, 16, 16)