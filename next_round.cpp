#include <iostream>

using namespace std;

int next_round() {
	int n, k;

	cin >> n >> k;

	int a;
	int count = 0;
	for (int i = 0; i < k; i++) {
		cin >> a;
		if (a == 0) {
			cout << i << endl;
			return 0;
		}
	}
	if (k == n) {
		cout << k << endl;
		return 0;
	}
	int ref;
	cin >> ref;
	for (int i = k; i < n; i++) {
		cin >> a;
		if (a < ref) {
			cout << k + (i - k) << endl;
			return 0;
		}
	}
	cout << n;
}
