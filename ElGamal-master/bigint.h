#include <vector>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

class bigint
{
	static const int OSN = 1000000000;                          // основание системы

	vector<int> elements;                                       // внутреннее хранилище числа

	bool sign;                                                  // знак числа

	bool odd() const;                                           // проверяет, является ли текущее число нечетным
	bool even() const;                                          // проверяет, является ли текущее число четным

	void removezeros();                                         // удаляет ведущие нули
	void shiftright();                                          // сдвигает все разряды на 1 вправо (домножает на OSN)

	bigint neg();                                                 // возвращает переданное число с другим знаком
public:
	class divzero : public exception { };                       // исключение при делении на ноль

	string __str__();
	string __repr__();
	string toString();

	bigint();                                                     // создает длинное целое число со значением 0
	bigint(string str);                                           // создает длинное целое число из строки
	bigint(int i);                                                // преобразует int к bigint
	operator string() const;                                    // преобразует число к строке

	string read(char* c);                                       // считывает строку с чиcлом из файла
	void write(string str, char* c);                            // записывает строку с числом в файл
	bigint readbin(char* c);                                      // считывает чиcло из бинарного файла
	void writebin(const bigint& b, char* c);                      // записывает число в бинарный файл

	friend ostream& operator <<(ostream& os, const bigint& b);    // печатает число в поток вывода
	friend istream& operator >>(istream& is, bigint& b);          // считывает число из потока ввода

	bool operator ==(const bigint& right);                        // сравнивает два числа на равенство
	bool operator !=(const bigint& right);                        // сравнивает два числа на неравенство
	bool operator <(const bigint& right);                         // проверяет, является ли левое число меньше правого
	bool operator >(const bigint& right);                         // проверяет, является ли левое число больше правого
	bool operator <=(const bigint& right);                        // проверяет, является ли левое число <= правого
	bool operator >=(const bigint& right);                        // проверяет, является ли левый число >= правого

	bigint operator +(const bigint& right) const;                   // складывает два числа
	bigint operator -(const bigint& right) const;                   // вычитает два числа
	bigint operator *(const bigint& right) const;                   // перемножает два числа
	bigint operator /(const bigint& right) const;                   // делит два числа
	bigint operator %(const bigint& right) const;                   // возвращает остаток от деления двух чисел
	bigint operator ^(const bigint& right) const;                   // возводит число в указанную степень
	bigint powmod(bigint& a, bigint& k, bigint& n);			    // возводит число в указанную степень по указанному модулю

	bigint operator +=(const bigint& right);                        // прибавляет к текущему числу новое
	bigint operator -=(const bigint& right);                        // вычитает из текущего числа новое
	bigint operator *=(const bigint& right);                        // умножает текущее число на указанное
	bigint operator /=(const bigint& right);                        // делит текущее число на указанное
	bigint operator %=(const bigint& right);                        // присваивает текущему числу остаток от деления на другое число
	bigint operator ^=(const bigint& right);                        // возводит текущее число в указанную степень

	bigint operator -() const;                                    // возвращает копию переданного числа с другим знаком
	bigint operator ++();                                         // префиксный инкремент
	bigint operator ++(int);                                      // постфиксный инкремент
	bigint operator --();                                         // префиксный декремент
	bigint operator --(int);                                      // постфиксный декремент
};
