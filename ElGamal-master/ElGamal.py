#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigint as lib
import sys
import random





def x_alg_E(a, b):
	
	if a == lib.bigint(0):
		return 0, 1, b

	if b == lib.bigint(0):
		return 1, 0, a

	px = lib.bigint(0)
	ppx = lib.bigint(1)
	py = lib.bigint(1)
	ppy = lib.bigint(0)

	while b > lib.bigint(0):
		q = a / b
		a, b = b, a % b
		x = ppx - q * px
		y = ppy - q * py
		ppx, px = px, x
		ppy, py = py, y

	return ppx, ppy, a


def inverse(a, p):
	x, y, g = x_alg_E(a, p)

	return (x % p + p) % p


def gen_keys():
	
	f = open("p.txt")

	p = int(f.read())

	f.close()

	prime_test(p)

	while True:
		g = random.randint(2, p - 1)

		if ((p - 1) % g) != 1:
			break

	x = random.randint(2, p - 1)

	p = lib.bigint(str(p))

	g = lib.bigint(str(g))

	x = lib.bigint(str(x))

	y = p.powmod(g, x, p)

	return p, g, y, x


def elgamal(msg, p, g, y, x):

	msg = lib.bigint(str(msg))

	if msg > p:
		raise ValueError("размер сообщения меньше p")

	pp = p.st()

	pp = int(pp)

	k = random.randint(2, pp - 1)

	k = lib.bigint(str(k))

	a = p.powmod(g, k, p)                                               # Кодирование

	b = p.powmod(y, k, p)                                               # Кодирование
	b = (msg * b) % p

	decode_msg = p.powmod(a, x, p)                                      # Декодирование
	decode_msg = inverse(decode_msg, p)
	decode_msg = (decode_msg * b) % p

	return decode_msg


def usage():
	print "\nИспользование: python ElG.py msg.txt\n"

	sys.exit(-1)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()

	f = open(sys.argv[1])

	msg = int(f.read())

	f.close()

	p, g, y, x = gen_keys()

	decode_msg = elgamal(msg, p, g, y, x)

	f = open("decode_msg.txt", "w")

	f.write(decode_msg.st())

	f.close()
