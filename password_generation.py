import random
lower = "abcdefghijklmnopqrstuvxz"
upper = "ABCDEFGHIJKLMNOPQRSTUVXZ"
num = "0123456789"
sybol = "@#$%¨&*"
all = lower + upper + num + sybol
# no length selecionar quantos caracteres vão ter o password
length = 10
password = "".join(random.sample(all,length))
print(password)