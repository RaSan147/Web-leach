# cython: language_level=3

cdef str c_seq = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-*/.,\\<>?;':\"[]{}|_=`~!@#$%^&() ’—"


cdef int seq[97][8]


seq = [[5, 8, 1, 7, 2, 4, 3, 6],
[7, 2, 1, 6, 3, 8, 4, 5],
[3, 6, 2, 4, 7, 5, 1, 8],
[1, 8, 3, 6, 5, 7, 4, 2],
[2, 7, 8, 5, 4, 1, 3, 6],
[3, 4, 6, 8, 1, 2, 5, 7],
[2, 7, 4, 8, 3, 5, 6, 1],
[8, 6, 1, 5, 4, 2, 7, 3],
[4, 8, 1, 6, 3, 2, 5, 7],
[1, 7, 8, 2, 3, 4, 6, 5],
[1, 8, 3, 6, 2, 4, 7, 5],
[1, 4, 2, 8, 5, 3, 6, 7],
[5, 4, 7, 8, 3, 2, 1, 6],
[8, 2, 1, 4, 5, 6, 3, 7],
[6, 5, 4, 7, 1, 8, 3, 2],
[5, 8, 7, 1, 4, 2, 6, 3],
[2, 6, 4, 8, 1, 7, 3, 5],
[6, 3, 7, 5, 4, 1, 2, 8],
[4, 5, 7, 2, 6, 1, 3, 8],
[7, 3, 6, 5, 2, 1, 8, 4],
[3, 6, 4, 5, 1, 8, 2, 7],
[5, 1, 2, 8, 4, 7, 6, 3],
[6, 4, 2, 1, 7, 3, 5, 8],
[5, 7, 4, 2, 6, 3, 1, 8],
[7, 1, 2, 5, 6, 3, 8, 4],
[4, 8, 2, 1, 5, 7, 3, 6],
[3, 5, 8, 7, 1, 2, 6, 4],
[7, 5, 6, 8, 4, 2, 3, 1],
[7, 2, 1, 6, 5, 3, 8, 4],
[6, 3, 1, 8, 7, 5, 4, 2],
[3, 1, 5, 8, 7, 6, 4, 2],
[8, 3, 1, 5, 7, 4, 2, 6],
[7, 5, 8, 1, 3, 6, 2, 4],
[7, 5, 1, 8, 4, 3, 6, 2],
[7, 2, 3, 1, 6, 5, 4, 8],
[1, 2, 6, 4, 8, 7, 3, 5],
[7, 6, 2, 5, 4, 3, 8, 1],
[2, 8, 5, 3, 7, 6, 1, 4],
[4, 3, 5, 6, 2, 8, 7, 1],
[8, 1, 6, 2, 7, 5, 3, 4],
[4, 8, 3, 6, 1, 5, 2, 7],
[3, 4, 7, 6, 2, 8, 5, 1],
[4, 5, 8, 3, 6, 1, 2, 7],
[5, 4, 6, 2, 3, 7, 8, 1],
[7, 4, 3, 5, 1, 6, 8, 2],
[7, 4, 1, 5, 3, 8, 2, 6],
[5, 2, 8, 3, 7, 1, 4, 6],
[8, 2, 5, 6, 1, 7, 4, 3],
[7, 5, 1, 4, 3, 6, 8, 2],
[8, 5, 4, 6, 1, 3, 2, 7],
[6, 5, 7, 4, 8, 2, 1, 3],
[8, 3, 1, 7, 5, 4, 6, 2],
[2, 6, 7, 8, 4, 3, 1, 5],
[5, 2, 7, 8, 4, 3, 6, 1],
[4, 6, 8, 3, 1, 5, 7, 2],
[5, 1, 6, 3, 8, 7, 4, 2],
[7, 6, 3, 5, 1, 4, 2, 8],
[6, 8, 2, 7, 3, 4, 5, 1],
[7, 3, 5, 4, 6, 8, 1, 2],
[5, 8, 3, 7, 2, 4, 1, 6],
[7, 8, 6, 2, 1, 4, 5, 3],
[4, 8, 1, 3, 5, 2, 6, 7],
[8, 6, 7, 2, 5, 4, 3, 1],
[5, 8, 4, 2, 6, 3, 7, 1],
[4, 8, 7, 5, 2, 1, 3, 6],
[7, 1, 4, 2, 5, 8, 3, 6],
[2, 5, 1, 3, 7, 4, 6, 8],
[3, 7, 1, 4, 8, 2, 6, 5],
[7, 5, 6, 4, 8, 2, 3, 1],
[3, 8, 4, 7, 6, 2, 5, 1],
[4, 6, 3, 5, 8, 1, 2, 7],
[7, 2, 8, 4, 1, 3, 5, 6],
[4, 6, 7, 2, 1, 3, 8, 5],
[8, 2, 1, 5, 6, 4, 7, 3],
[6, 8, 5, 2, 4, 7, 3, 1],
[3, 7, 6, 8, 1, 5, 4, 2],
[3, 8, 1, 7, 5, 2, 6, 4],
[7, 2, 5, 6, 4, 3, 1, 8],
[3, 4, 1, 8, 2, 7, 5, 6],
[4, 7, 6, 2, 5, 1, 3, 8],
[6, 1, 3, 2, 5, 4, 7, 8],
[8, 4, 3, 5, 7, 2, 6, 1],
[3, 5, 6, 7, 1, 2, 8, 4],
[1, 3, 8, 6, 2, 7, 5, 4],
[5, 4, 1, 7, 6, 3, 8, 2],
[6, 3, 2, 1, 4, 5, 7, 8],
[3, 4, 5, 8, 7, 1, 2, 6],
[5, 6, 3, 8, 4, 2, 7, 1],
[7, 3, 4, 2, 5, 6, 8, 1],
[4, 6, 1, 3, 7, 2, 8, 5],
[1, 3, 6, 2, 8, 5, 7, 4],
[7, 1, 8, 5, 6, 4, 3, 2],
[3, 1, 5, 2, 8, 4, 6, 7],
[8, 5, 2, 4, 3, 1, 6, 7],
[2, 8, 7, 1, 4, 5, 3, 6],
[6, 5, 7, 3, 4, 8, 1, 2],
[3, 2, 8, 4, 6, 5, 7, 1]]



cdef list _encrypt(list text, list C):
	cdef int i
	i=0
	cdef int j
	cdef int le
	le=len(text)
	cdef int x
	cdef list back

	while i<le:
		back=text[i:i+8]
		x=0
		for j in range(8):
			#print('i+x',i+x,'\tj',j-1)
			text[i+x]=back[C[j]-1]
			x=(x+1)%8

		i+=8
	return text


cdef list _decrypt(list text, list C):

	cdef int i=0
	cdef int le=len(text)
	cdef list back
	while i<le:
		x=0
		back=text[i:i+8]
		for j in range(8):
			text[i+ C[j]-1]=back[x]
			x=(x+1)%8
		i+=8
	return text


cpdef str CYencrypt(str texts, str key, str typer='str'):
	"""
	text: text data to decrypt
	key: key to decrypt
	typer: str or list (only available for str)
	"""
	cdef list returner = []
	cdef list text_
	cdef int c[8]
	cdef int i

	cdef str text
	cdef str a

	for text in texts.splitlines():
		text+=" "*((8-len(text)%8)%8)

		text_=list(text)
		for a in key:
			c = seq[c_seq.find(a)]
			text_=text_[2:]+text_[:2]
			text_= _encrypt(text_, c)
		returner.append("".join(text_))

	
	return ('\n'.join(returner))


cpdef str CYdecrypt(str texts, str key, str typer= "str"):
	"""
	text: text data to decrypt
	key: key to decrypt
	typer: str or list (only available for str)
	"""
	cdef list returner = []
	cdef list text_
	cdef int c[8]
	cdef int i
	cdef list dtext_
	
	
	key=key[::-1]

	for text in texts.splitlines():
		text+=" "*((8-len(text)%8)%8)
		dtext_=list(text)
		

		for i in range(len(key)):
			c= seq[c_seq.index(key[i])]
			dtext_=_decrypt(dtext_, c)
			dtext_=dtext_[-2:]+dtext_[:-2]

		returner.append("".join(dtext_))

	return ('\n'.join(returner))
