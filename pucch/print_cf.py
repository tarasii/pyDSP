import sys 


fname = sys.argv[1]
with open(fname) as f:
  txt = f.read().splitlines()


print(f"format:{int(txt[0],16)} ({txt[0]})") 
print(f"NRB:{int(txt[1],16)} ({txt[1]})") 
print(f"ofdm_symbol_size:{int(txt[2],16)} ({txt[2]})") 
print(f"first_carrier_offset:{int(txt[3],16)} ({txt[3]})") 
print(f"start_symbol_index:{int(txt[4],16)} ({txt[4]})") 
print(f"nrofsymbols:{int(txt[5],16)} ({txt[5]})") 
print(f"startRB:{int(txt[6],16)} ({txt[6]})") 
print(f"startPRB:{int(txt[7],16)} ({txt[7]})") 
print(f"hoppingID:{int(txt[8],16)} ({txt[8]})") 
print(f"GroupHopping:{int(txt[9],16)} ({txt[9]})") 
print(f"SecondHopPRB:{int(txt[10],16)} ({txt[10]})") 
print(f"InitialCS:{int(txt[11],16)} ({txt[11]})") 
print(f"ACK:{int(txt[12],16)} ({txt[12]})") 
print(f"sr:{int(txt[13],16)} ({txt[13]})") 
print(f"nr_bit:{int(txt[14],16)} ({txt[14]})") 
print(f"sr_flag:{int(txt[15],16)} ({txt[15]})") 
print(f"InterSlotFreqHopping:{int(txt[16],16)} ({txt[16]})") 
print(f"IntraSlotFreqHopping:{int(txt[17],16)} ({txt[17]})") 
print(f"time_domain_occ_idx:{int(txt[18],16)} ({txt[18]})") 
print(f"nr_slot_tx:{int(txt[19],16)} ({txt[19]})") 
print(f"NTX:{int(txt[20],16)} ({txt[20]})") 
