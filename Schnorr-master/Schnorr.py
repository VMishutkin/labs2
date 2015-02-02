#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigint as lib
import sys
import random


def x_alg_E(a, b):
	
	if a == lib.BigInt(0):
		return 0, 1, b

	if b == lib.BigInt(0):
		return 1, 0, a

	px = lib.BigInt(0)
	ppx = lib.BigInt(1)
	py = lib.BigInt(1)
	ppy = lib.BigInt(0)

	while b > lib.BigInt(0):
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

	f = open("q.txt")

	q = int(f.read())

	f.close()

	f = open("g.txt")

	g = int(f.read())

	f.close()


	w = random.randint(2, q - 1)
	r = random.randint(2, q - 1)

	p = lib.BigInt(str(p))
	q = lib.BigInt(str(q))
	g = lib.BigInt(str(g))
	w = lib.BigInt(str(w))
	r = lib.BigInt(str(r))

	inv_g = inverse(g, p)

	y = p.powmod(inv_g, w, p)

	x = p.powmod(g, r, p)

	print "\nКлючи сгенерированы:\n"

	print "x = ", x, "отсылается Михаилу\n"

	return p, q, g, w, r, y, x


def schnorr(p, q, g, w, r, y, x):
	e = random.randint(0, pow(2, 20) - 1)

	e = lib.BigInt(str(e))

	print "e = ", e, "отсылается Алексею\n"

	s = (r + w * e) % q

	print "s = ", s, "отсылается Андрей\n"

	m1 = p.powmod(g, s, p)
	m2 = p.powmod(y, e, p)

	m = (m1 * m2) % p

	if m == x:
		print "Андрей подтвердил", m, "\n"
	else:
		print "Косяк\n"


if __name__ == "__main__":
	p, q, g, w, r, y, x = gen_keys()

	schnorr(p, q, g, w, r, y, x)
