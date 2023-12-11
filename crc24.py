CRC_24A_INITIALIZATION = 0
CRC_24A_POLYNOM = 0x864cfb #1000 0110 0100 1100 1111 1011


def crcbit(octet, crc, poly):
    """simple CRC operation"""
    crc ^= (octet << 16)
    for i in range(8):
        crc <<= 1
        if crc & 0x1000000: crc ^= poly
    return crc 

def crcbit_1(octet, crc, poly):
    c = (octet << 16)
    for i in range(8):
        if (c ^ crc) & 0x800000:
            crc <<= 1 
            crc ^= poly
        else:
            crc <<= 1
        c <<= 1
    return crc 
       
def crc24_8bit_data_uni(octets, poly, init):

    crc = init
    for octet in octets: 
        crc = crcbit(octet, crc, poly)

    return crc & 0xFFFFFF #24bit mask

def crc24_8bit_data_tb_init(poly):
    """
    This function generates CRC_24A_TABLE
    """
    crc_tb = []
    for c0 in range(256):

        #crc = crcbit_1(c0, 0, poly)
        crc = crcbit(c0, 0, poly)

        crc_tb.append(crc & 0x00ffffff)
    return crc_tb

CRC_24_INITIALIZATION = 0x00b704ce
CRC_24_POLY = 0x1864CFB

CRC_24A_TABLE = (
    0x000000, 0x864cfb, 0x8ad50d, 0x0c99f6, 0x93e6e1, 0x15aa1a, 0x1933ec,
    0x9f7f17, 0xa18139, 0x27cdc2, 0x2b5434, 0xad18cf, 0x3267d8, 0xb42b23,
    0xb8b2d5, 0x3efe2e, 0xc54e89, 0x430272, 0x4f9b84, 0xc9d77f, 0x56a868,
    0xd0e493, 0xdc7d65, 0x5a319e, 0x64cfb0, 0xe2834b, 0xee1abd, 0x685646,
    0xf72951, 0x7165aa, 0x7dfc5c, 0xfbb0a7, 0x0cd1e9, 0x8a9d12, 0x8604e4,
    0x00481f, 0x9f3708, 0x197bf3, 0x15e205, 0x93aefe, 0xad50d0, 0x2b1c2b,
    0x2785dd, 0xa1c926, 0x3eb631, 0xb8faca, 0xb4633c, 0x322fc7, 0xc99f60,
    0x4fd39b, 0x434a6d, 0xc50696, 0x5a7981, 0xdc357a, 0xd0ac8c, 0x56e077,
    0x681e59, 0xee52a2, 0xe2cb54, 0x6487af, 0xfbf8b8, 0x7db443, 0x712db5,
    0xf7614e, 0x19a3d2, 0x9fef29, 0x9376df, 0x153a24, 0x8a4533, 0x0c09c8,
    0x00903e, 0x86dcc5, 0xb822eb, 0x3e6e10, 0x32f7e6, 0xb4bb1d, 0x2bc40a,
    0xad88f1, 0xa11107, 0x275dfc, 0xdced5b, 0x5aa1a0, 0x563856, 0xd074ad,
    0x4f0bba, 0xc94741, 0xc5deb7, 0x43924c, 0x7d6c62, 0xfb2099, 0xf7b96f,
    0x71f594, 0xee8a83, 0x68c678, 0x645f8e, 0xe21375, 0x15723b, 0x933ec0,
    0x9fa736, 0x19ebcd, 0x8694da, 0x00d821, 0x0c41d7, 0x8a0d2c, 0xb4f302,
    0x32bff9, 0x3e260f, 0xb86af4, 0x2715e3, 0xa15918, 0xadc0ee, 0x2b8c15,
    0xd03cb2, 0x567049, 0x5ae9bf, 0xdca544, 0x43da53, 0xc596a8, 0xc90f5e,
    0x4f43a5, 0x71bd8b, 0xf7f170, 0xfb6886, 0x7d247d, 0xe25b6a, 0x641791,
    0x688e67, 0xeec29c, 0x3347a4, 0xb50b5f, 0xb992a9, 0x3fde52, 0xa0a145,
    0x26edbe, 0x2a7448, 0xac38b3, 0x92c69d, 0x148a66, 0x181390, 0x9e5f6b,
    0x01207c, 0x876c87, 0x8bf571, 0x0db98a, 0xf6092d, 0x7045d6, 0x7cdc20,
    0xfa90db, 0x65efcc, 0xe3a337, 0xef3ac1, 0x69763a, 0x578814, 0xd1c4ef,
    0xdd5d19, 0x5b11e2, 0xc46ef5, 0x42220e, 0x4ebbf8, 0xc8f703, 0x3f964d,
    0xb9dab6, 0xb54340, 0x330fbb, 0xac70ac, 0x2a3c57, 0x26a5a1, 0xa0e95a,
    0x9e1774, 0x185b8f, 0x14c279, 0x928e82, 0x0df195, 0x8bbd6e, 0x872498,
    0x016863, 0xfad8c4, 0x7c943f, 0x700dc9, 0xf64132, 0x693e25, 0xef72de,
    0xe3eb28, 0x65a7d3, 0x5b59fd, 0xdd1506, 0xd18cf0, 0x57c00b, 0xc8bf1c,
    0x4ef3e7, 0x426a11, 0xc426ea, 0x2ae476, 0xaca88d, 0xa0317b, 0x267d80,
    0xb90297, 0x3f4e6c, 0x33d79a, 0xb59b61, 0x8b654f, 0x0d29b4, 0x01b042,
    0x87fcb9, 0x1883ae, 0x9ecf55, 0x9256a3, 0x141a58, 0xefaaff, 0x69e604,
    0x657ff2, 0xe33309, 0x7c4c1e, 0xfa00e5, 0xf69913, 0x70d5e8, 0x4e2bc6,
    0xc8673d, 0xc4fecb, 0x42b230, 0xddcd27, 0x5b81dc, 0x57182a, 0xd154d1,
    0x26359f, 0xa07964, 0xace092, 0x2aac69, 0xb5d37e, 0x339f85, 0x3f0673,
    0xb94a88, 0x87b4a6, 0x01f85d, 0x0d61ab, 0x8b2d50, 0x145247, 0x921ebc,
    0x9e874a, 0x18cbb1, 0xe37b16, 0x6537ed, 0x69ae1b, 0xefe2e0, 0x709df7,
    0xf6d10c, 0xfa48fa, 0x7c0401, 0x42fa2f, 0xc4b6d4, 0xc82f22, 0x4e63d9,
    0xd11cce, 0x575035, 0x5bc9c3, 0xdd8538
)

def crc24_opt(data, table, init):
    result = init
    for byte in data:
        index = ((result >> 16) ^ byte) & 0xff
        result = (table[index] ^ (result << 8)) & 0x00ffffff
    return result

def crc24a_smpl(data):
    return crc24_8bit_data_uni(data, CRC_24A_POLYNOM, CRC_24A_INITIALIZATION)

def crc24a(data):
    return crc24_opt(data, CRC_24A_TABLE, CRC_24A_INITIALIZATION)

crc24a_table = crc24_8bit_data_tb_init(CRC_24A_POLYNOM)

def crc24a_dyn(data):
    return crc24_opt(data, crc24a_table, CRC_24A_INITIALIZATION)


def crcbitrev(octet, crc, poly):
    crc ^= octet 
    for i in range(8): 
        if crc & 1: 
            crc >>= 1
            crc ^= poly
        else:
            crc >>= 1

    return crc 

def crc24a_rev(octets):
    poly24ar = rot24(CRC_24A_POLYNOM)
    crc = 0
    for octet in octets: 
        crc = crcbitrev(octet, crc, poly24ar)

    return crc & 0xFFFFFF

def crc24_8bit_data_rev_tb_init(poly):
    crc_tb = []
    for c0 in range(256):
        crc = crcbitrev(c0, 0, poly)

        crc_tb.append(crc & 0x00ffffff)
    return crc_tb

def rot24(inp):
    ret = ((inp & 0x000001) << 23) | \
          ((inp & 0x000002) << 21) | \
          ((inp & 0x000004) << 19) | \
          ((inp & 0x000008) << 17) | \
          ((inp & 0x000010) << 15) | \
          ((inp & 0x000020) << 13) | \
          ((inp & 0x000040) << 11) | \
          ((inp & 0x000080) << 9)  | \
          ((inp & 0x000100) << 7)  | \
          ((inp & 0x000200) << 5)  | \
          ((inp & 0x000400) << 3)  | \
          ((inp & 0x000800) << 1)  | \
          ((inp & 0x001000) >> 1)  | \
          ((inp & 0x002000) >> 3)  | \
          ((inp & 0x004000) >> 5)  | \
          ((inp & 0x008000) >> 7)  | \
          ((inp & 0x010000) >> 9)  | \
          ((inp & 0x020000) >> 11) | \
          ((inp & 0x040000) >> 13) | \
          ((inp & 0x080000) >> 15) | \
          ((inp & 0x100000) >> 17) | \
          ((inp & 0x200000) >> 19) | \
          ((inp & 0x400000) >> 21) | \
          ((inp & 0x800000) >> 23)
    return ret

crc24a_rev_table = crc24_8bit_data_rev_tb_init(rot24(CRC_24A_POLYNOM))

def crc24_opt_rev(data, table, init):
    result = init
    for byte in data:
        index = (result ^ byte) & 0xff
        result = (table[index] ^ (result >> 8) ) & 0x00ffffff
    return result

def rot8(inp):
    ret = ((inp & 0x01) << 7) | \
          ((inp & 0x02) << 5) | \
          ((inp & 0x04) << 3) | \
          ((inp & 0x08) << 1) | \
          ((inp & 0x10) >> 1) | \
          ((inp & 0x20) >> 3) | \
          ((inp & 0x40) >> 5) | \
          ((inp & 0x80) >> 7)
    return ret 

def check_result_str(inp, res):
    return "Ok" if (inp == res) else "wrong"


with open("PUSCH_TV_iter10_slot2_ue2_pusch1_ldpc_tb.dat", mode="rb") as inp_file:
    contents = inp_file.read()
    
    crc_ref = 0x7fa2b1 #reference crc for PUSCH_TV_iter10_slot2_ue2_pusch1_ldpc_tb.dat
    print (f"{hex(crc_ref)}, crc24a ref {bin(crc_ref)}")
    
    crc = crc24a_smpl(contents) 
    print (f"{hex(crc)}, crc24a simple function: {check_result_str(crc, crc_ref)}")
    
    crc = crc24a(contents) 
    print (f"{hex(crc)}, crc24a function with static LUT: {check_result_str(crc, crc_ref)}")
    
    crc = crc24a_dyn(contents) 
    print (f"{hex(crc)}, crc24a function with dynamic LUT: {check_result_str(crc, crc_ref)}")

    contents_r = [rot8(x) for x in contents]

    crc_ref = 0x96eaba
    crc = crc24a(contents_r) 
    print (f"{hex(crc)}, crc24a for input with rotated bits in byte: {check_result_str(crc, crc_ref)}")
    print (f"{hex(rot24(crc))}, crc24a rotated for input with rotated bits in byte: {check_result_str(rot24(crc), rot24(crc_ref))}")

    crc = crc24a_rev(contents)
    print (f"{hex(crc)}, crc24a rotared function for normal bit order input: {check_result_str(crc, rot24(crc_ref))}")

    crc = crc24_opt_rev(contents, crc24a_rev_table, 0)
    print (f"{hex(crc)}, crc24a rotared LUT function for normal bit order input: {check_result_str(crc, rot24(crc_ref))}")


#wiki example
def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]

crc = crc_remainder('11010011101100', '1011', '0')
#print(crc)

#crc = crc_remainder('11111111111000010001110110011010', '101101110000010011001110', '0')
#print(crc)
#0xb0aed7
#1011 0000 1010 1110 1101 0111

