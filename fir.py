import numpy as np 
import util
from scipy.signal import lfilter


def fir_t(A, coef, n, tap):
	res = np.zeros(n+tap, np.complex)
	tmp = np.zeros(n, np.complex)
	tmp[0:n] = A[0:n]
	for i in range(0, tap):
		res[i:i+n] = res[i:i+n] + tmp*coef[i]

	return res

def fir(A, coef, n, tap):
	res = np.zeros(n+tap, np.complex)
	tmp = np.zeros(tap, np.complex)
	tmp[0:tap] = coef[0:tap]
	for i in range(0, n):
		res[i:i+tap] = res[i:i+tap] + A[i]*tmp

	return res

def fir6tap(A, coef, n):
		fir(A, coef, n, 6)

def fir7tap(A, coef, n):
		fir(A, coef, n, 7)

def fir8tap(A, coef, n):
		fir(A, coef, n, 8)

def fir12tap(A, coef, n):
		fir(A, coef, n, 12)

if __name__ == '__main__':
	fn = "fir_x.in"
	dt_in = util.load_file(fn)

	dt_in = [x + y*1j for x, y in dt_in]

	fn = "fir_coefs.in"
	coef = util.load_file(fn)
	coef = [x + y*1j for x, y in coef]

	res = fir(dt_in, coef, 128, 65)

	print(res[0:20])

	res = lfilter(coef[0:65], 1.0, dt_in)
	print(res[0:20])
