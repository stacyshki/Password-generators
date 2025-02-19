import random as r
import string

pwd_len = 0

while pwd_len < 16:
    pwd_len = int(input('Pass length:'))

uppercase_char = string.ascii_uppercase
lowercase_char = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

combined_list = uppercase_char + lowercase_char + digits + symbols
rnd_up_ch = r.choice(uppercase_char)
rnd_lw_ch = r.choice(lowercase_char)
rnd_dig_ch = r.choice(digits)
rnd_sy_ch = r.choice(symbols)

temp_pwd = r.sample(combined_list, pwd_len - 4)
r.shuffle(temp_pwd)
print(*temp_pwd, sep='')