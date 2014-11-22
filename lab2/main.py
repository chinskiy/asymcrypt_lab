import lab2.rsa_all as l2
import lab1.ps_rand_numb as gener
import time


abon_a, abon_b = l2.build_rsa(256), l2.build_rsa(256)
if abon_a['p'] * abon_a['q'] > abon_b['p'] * abon_b['q']:
    abon_a, abon_b = abon_b, abon_a
m = int(gener.BBSbyte().genseqbin(100), 2)
# l2.check_rsa_encr_decr(abon_a, m)
# l2.create_and_check_rsa_sign(abon_a, m)
# l2.chech_protocol_conf_key_sending(abon_a, abon_b, m)