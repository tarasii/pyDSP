import sys 


def read_cf(fname):
  with open(fname) as f:
    txt = f.read().splitlines()
    
  d = {
      "format":int(txt[0],16), 
      "NRB":int(txt[1],16), 
      "ofdm_symbol_size":int(txt[2],16),
      "first_carrier_offset":int(txt[3],16),
      "start_symbol_index":int(txt[4],16),
      "nrofsymbols":int(txt[5],16),
      "startRB":int(txt[6],16),
      "startPRB":int(txt[7],16),
      "hoppingID":int(txt[8],16),
      "GroupHopping":int(txt[9],16),
      "SecondHopPRB":int(txt[10],16),
      "InitialCS":int(txt[11],16),
      "ACK":int(txt[12],16),
      "sr":int(txt[13],16),
      "nr_bit":int(txt[14],16),
      "sr_flag":int(txt[15],16),
      "InterSlotFreqHopping":int(txt[16],16),
      "IntraSlotFreqHopping":int(txt[17],16),
      "time_domain_occ_idx":int(txt[18],16),
      "nr_slot_tx":int(txt[19],16),
      "NTX":int(txt[20],16),
  }
  return d 
  

  
if __name__ == '__main__':  
  fname = sys.argv[1]
  d = read_cf(fname)
  print(d)