def generate_n_chars(n,c):
    res = ''
    for i in range(n):
	res+=c
    return res

print(generate_n_chars(5,'x'))
