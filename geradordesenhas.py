import random, string
tamanho = 16
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-+=,.;:/?'
rdm = random.SystemRandom()
print("Password: " + ''.join(rdm.choice(chars) for i in range(tamanho)))
