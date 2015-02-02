RSA:
	swig -c++ -python bigint.i
	g++ -fPIC -c bigint.cpp
	g++ -fPIC -c bigint_wrap.cxx -I/usr/include/python2.7
	g++ -shared bigint.o bigint_wrap.o -o _bigint.so
	rm bigint.o bigint_wrap.cxx bigint_wrap.o
