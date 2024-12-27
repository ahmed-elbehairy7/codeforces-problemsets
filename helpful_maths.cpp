#include <iostream>

using namespace std;

int main() {
	string s;
	cin >> s;

	int ones, twos, threes;
	ones = twos = threes = 0;
	int len = s.length();
	for (int i = 0; i < len; i++) {
		if (s[i] == '1') {
			ones++;
		}
		if (s[i] == '2') {
			twos++;
		}
		if (s[i] == '3') {
			threes++;
		}
	}

	bool b = false;

	for (int i = 0; i < ones; i++) {
		if (b) {
			cout << '+';
		}
		b = true;
		cout << 1;
	}
	for (int i = 0; i < twos; i++) {
		if (b) {
			cout << '+';
		}
		b = true;
		cout << 2;
	}
	for (int i = 0; i < threes; i++) {
		if (b) {
			cout << '+';
		}
		b = true;
		cout << 3;
	}
}