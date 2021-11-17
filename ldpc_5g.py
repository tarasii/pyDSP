
import pcm

max_zc = 384

pcmt = pcm.init_pcm()


def read_buf(fnin):
  with open(fnin) as f:
    txt = f.readlines()
  
  res = []
  zc = int(txt[0].replace("ZC: ",""))
  i_ls = int(txt[1].replace("INDEX: ",""))
  for x in txt[2:]:
    z = int(x, 16)
    res.append(z)

  return zc, i_ls, res


def write_buf(p_out, fnout):

  with open(fnout,"w") as f:
    for x in p_out:
      f.write(hex(x))
      f.write("\n")


def to_bits(p_inp):
  l = []
  for x in p_inp:
    bs = format(x, '032b')
    for y in bs[::-1]:
    	l.append(int(y))

  return l

def from_bits(z):
  ret = 0
  k = 1;
  for x in z:
    ret = ret + x * k
    k = k * 2

  return ret 

def from_bits_vec(p_data, l):
  tmp = []
  for x in range(0, l):
    tmp.append(from_bits(p_data[x*32:(x+1)*32]))

  return tmp


def print_vec_hex(p_data, l):
  tmp = from_bits_vec(p_data, l)

  for x in tmp:
    print(hex(x), " ", end = '')

  print("") 


def cyc_shift(p_inp, shift):
  return p_inp[shift:]+p_inp[:shift]


def xor(a, b):
  c = []
  for x,y in zip(a,b):
    c.append(x ^ y)

  return c

def add_shift(in_p, srow, erow, scol, ecol):
  res = []
  for i in range(srow, erow):
    r = [0] * zc
    c_num = pcmt[bg][i].cnum
    for j in range(0, c_num):
      #print(i,j)
      in_col = pcmt[bg][i].col[j].cidx

      shift = pcmt[bg][i].col[j].csval[i_ls]

      if (in_col >= scol and in_col < ecol):
        sh = cyc_shift(in_p[in_col - scol], shift % zc)
        r = xor(r, sh)

    res.append(r) 

  return res 


def ldpc_encoder(s, bg, i_ls):

  nrows, ncols, ah, kb = pcm.get_defs(bg)

  _as = add_shift(s, 0, ah, 0, kb)
  _cs = add_shift(s, ah, nrows, 0, kb)
	
  if (bg==1):

    p10 = xor(_as[0], _as[1])
    p10 = xor(p10, _as[2])
    p10 = xor(p10, _as[3])

    sh = pcm.get_shift(bg, i_ls, 0, kb)
    p10_sh = cyc_shift(p10, sh)
    p11 = xor(_as[0], p10_sh)

    p12 = xor(_as[2], _as[3])
    p12 = xor(p12, p10_sh)

    p13 = xor(_as[3], p10_sh)

    p14 = _as[4]

    _p1 = [p10, p11, p12, p13, p14]

  else:

    p10 = xor(_as[0], _as[1])
    p10 = xor(p10, _as[2])
    p10 = xor(p10, _as[3])
    a0_sh = pcm.get_shift(bg, i_ls, 2, kb)
    p10 = cyc_shift(p10, -a0_sh)

    p11 = xor(_as[0], p10)

    x_sh = pcm.get_shift(bg, i_ls, 4, kb+1)
    y_sh = pcm.get_shift(bg, i_ls, 5, kb+1)
    z_sh = pcm.get_shift(bg, i_ls, 6, kb+1)

    p12 = xor(_as[1], p11)

    p13 = xor(_as[3], p10)

    tmp = cyc_shift(p11, x_sh)
    p14 = xor(_as[4], tmp)

    tmp = cyc_shift(p11, y_sh)
    p15 = xor(_as[5], tmp)

    tmp = cyc_shift(p11, z_sh)
    p16 = xor(_as[6], tmp)

    _p1 = [p10, p11, p12, p13, p14, p15, p16]


  _dp =  add_shift(_p1, ah, nrows, kb, kb+ah)

  #P2 = CS+DP
  _p2 = []
  for x, y in zip(_cs, _dp):
    _p2.append(xor(x, y))

  res = s[2:] + _p1 + _p2

  return res

if (__name__== "__main__"):
  #fn_in = "test_51_data.inp"
  #fn_out = "test_bg1_51_enc.pout"

  fn_in = "test_43_data.inp"
  fn_out = "test_bg1_43_enc.pout"

  bg = 1
  zc, i_ls, p_inp = read_buf(fn_in)
  dt_inp = to_bits(p_inp)

  nrows, ncols, ah, kb = pcm.get_defs(bg)
  block_length = kb * zc

  print("ZC:{} BG:{} I_ls:{} {} nrows:{} kb:{} block_length:{}".format(zc, bg, i_ls, pcm.get_i_ls(zc), nrows, kb, block_length ))
  print("datalen:{}".format(len(dt_inp)))

  s = []
  for i in range(0, kb):
  	s.append(dt_inp[i*zc:(i+1)*zc])

  res = ldpc_encoder(s, bg, i_ls)

  out = []
  for x in res:
    tmp = from_bits_vec(x, int(zc/32)) 
    for y in tmp:
      out.append(y)

  write_buf(out, fn_out)
