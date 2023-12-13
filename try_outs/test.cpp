#include "bits/stdc++.h"

using namespace std;

struct node{
	int64_t invs = 0;
	vector<int> f = vector <int> (40, 0);

	void combine(const node& left, const node& right){
		invs = left.invs+right.invs;
		for (int i=0; i<40; i++){
			f[i] = left.f[i] + right.f[i];
			if (right.f[i] != 0){
				for (int j=i+1; j<40; j++){
					if (left.f[j] != 0){
						invs += (1LL*right.f[i]*left.f[j]);
					}
				}
			}
		}
	}
};


void build(vector <node>& st, vector <int>& a, int tl, int tr, int pos){
	if (tl == tr){
		st[pos].invs = 0;
		st[pos].f[a[tl]] = 1;
	}
	else{
		int tm = (tl+tr)/2;
		build(st, a, tl, tm, 2*pos);
		build(st, a, tm+1, tr, 2*pos+1);
		st[pos].combine(st[2*pos], st[2*pos+1]);
	}
}

void update(vector <node>& st, int i, int val, int tl, int tr, int pos){
	if (tl == tr){
		st[pos].invs = 0;
		st[pos].f = vector <int> (40, 0);
		st[pos].f[val] = 1;
	}
	else{
		int tm = (tl + tr)/2;
		if (i <= tm){
			update(st, i, val, tl, tm, 2*pos);
		}
		else{
			update(st, i, val, tm+1, tr, 2*pos+1);
		}
		st[pos].combine(st[2*pos], st[2*pos+1]);
	}
}

node query(vector <node>& st, int l, int r, int tl, int tr, int pos){
	if (l > r){
		return node();
	}
	if (tl == l and tr == r){
		return st[pos];
	}
	int tm = (tl+tr)/2;
	node ans;
	ans.combine(query(st, l, min(r, tm), tl, tm, 2*pos), query(st, max(l, tm+1), r, tm+1, tr, 2*pos+1));
	return ans;
}

void solve(){
	int n, q;
	cin >> n >> q;

	vector <int> a(n);
	for (int i=0; i<n; ++i){
		cin >> a[i];
		-- a[i];
	}
	vector <node> st(4*n);
	build(st, a, 0, n-1, 1);

	for (int i=0; i<q; i++){
		int type, x, y;
		cin >> type >> x >> y;
		--x;
		--y;

		if (type == 1){
			node ans = query(st, x, y, 0, n-1, 1);
			cout << ans.invs <<'\n';
		}
		else{
			update(st, x, y, 0, n-1, 1);
		}
	}
}

int main(){
	std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.precision(10);
    std::cout << std::fixed << std::boolalpha;
    
    solve();

    return 0;
}
