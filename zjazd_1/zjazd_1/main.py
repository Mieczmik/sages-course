import data_prep.prepare_str as prst
from data_models.stat_model import count_len

napis = 'znaki1$'
prst.remove_spec_char(napis)
prst.remove_digit_one()
count_len(napis)