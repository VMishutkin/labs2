#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigint as lib
import sys
import random

def x_alg_E(a, b):
	"""Расширенный алгоритм Евклида

	"""
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


def gen_d(a, b):
	
	while True:
		x, y, g = x_alg_E(a, b)

		if g != lib.bigint(1):
			raise ValueError("Невозможно подобрать d")
		else:
			z = x % b
			break
	return z


def rsa(msg, p, q, e):

	msg = lib.bigint(str(msg))

	modulus = p * q

	fi = (p - lib.bigint(1)) * (q - lib.bigint(1))

	if msg > modulus:
		raise ValueError("Неверная длина сообщения")

	d = gen_d(e, fi)

	encoding = d.powmod(msg, e, modulus)                      # Кодирование

	decode = d.powmod(encoding, d, modulus)               # Декодирование

	return decode


def usage():
	print "\nИспользование: python RSA.py msg.txt\n"

	sys.exit(-1)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()

	f = open(sys.argv[1])

	msg = int(f.read())

	f.close()

	tmp = lib.bigint()

	p = lib.bigint(tmp.read("p.txt"))
	q = lib.bigint(tmp.read("q.txt"))
	e = lib.bigint(tmp.read("e.txt"))

	

	decode = rsa(msg, p, q, e)

	f = open("decode_msg.txt", "w")
	f.write("текст после расшифровки\n")
	f.write(decode.st())

	f.close()
