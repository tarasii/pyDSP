import numpy as np 
import util
from scipy.signal import lfilter

def fir_s(dt, coef, shift=0):
	""" simple FIR function """

	n = len(dt)	
	ntap = len(coef)
	res = np.zeros(n, np.complex)

	# insert zeros for FIR preroll
	dtx = np.append(np.zeros(ntap-1, np.complex), dt)

	for i in range(0, n):
		res[i] = np.sum(dtx[i:i+ntap]*coef[::-1])

	return res / 2**shift


def fir_t(A, coef, shift=0):
	n = len(A)
	tap = len(coef)	
	res = np.zeros(n+tap, np.complex)
	tmp = np.zeros(n, np.complex)
	tmp[0:n] = A[0:n]
	tap = len(coef)
	for i in range(0, tap):
		res[i:i+n] = res[i:i+n] + tmp*coef[i]

	return res[:len(A)]/2**shift


def fir(A, coef, shift=0):
	n = len(A)
	tap = len(coef)
	res = np.zeros(n+tap, np.complex)

	for i in range(0, n):
		res[i:i+tap] = res[i:i+tap] + A[i]*coef

	return res[:len(A)]/2**shift


def fir6tap(A, coef):
		fir(A, coef[:6])

def fir7tap(A, coef):
		fir(A, coef[:7])

def fir8tap(A, coef):
		fir(A, coef[:8])

def fir12tap(A, coef):
		fir(A, coef[:12])

if __name__ == '__main__':
	fn = "fir_x.in"
	dt_in = util.load_complex(fn)


	fn = "fir_coefs.in"
	coef = util.load_complex(fn)

	res = fir_s(dt_in[:128], coef[:65])

	ref = lfilter(coef[:65], 1.0, dt_in)

	diff = res - ref
	diff = np.absolute(diff)
	diff = diff[diff > 0]
	print(f"Values count with difference: {len(diff)}")


