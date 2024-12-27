#include <iostream>

using namespace std;

int peya_and_strings() {
	string a, b;
	cin >> a >> b;
	for (int i = 0; i < a.length(); i++) {
		char achar = tolower(a[i]);
		char bchar = tolower(b[i]);
		if (achar > bchar) {
			cout << 1 << endl;
			return 0;
		}
		else if (achar < bchar) {
			cout << -1 << endl;
			return 0;
		}
		
	}
	cout << 0;
}