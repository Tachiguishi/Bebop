
/*
 *  Name : BC42D.cpp
 *  Author : CHN.ChouUn
 *  Date : 2015年5月24日 上午9:38:04
 *  Copyright : www.fateud.com
 *  Description : None
 *  http://acm.hdu.edu.cn/showproblem.php?pid=5235
 */

#include <csl_std.h>
#include <bigint.h>
//@ Using Namespace
//@ Program Begin

#define maxN 4010
#define maxT 60010
#define maxD 100000
typedef csl::BigInt<45> bint;

struct node {
  int64 n;
  int k;
  int idx;
  int64 ret;

  static bool
  cmpk(const node& a, const node& b)
  { return a.k < b.k; }

  static bool
  cmpi(const node& a, const node& b)
  { return a.idx < b.idx; }

};

int T;
node a[maxT];
bint f[maxN];
int64 dp[maxN];
int g[maxD];

void Init() {
  f[0] = 0;
  f[1] = 1;
  dp[0] = 0;
  g[0] = 0;
  for (int i = 1; i < maxD; i++)
    g[i] = g[i/10] + i%10;
}

void Input() {
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf(i64"%d", &a[i].n, &a[i].k);
    a[i].idx = i;
    a[i].ret = 0;
  }
  std::sort(a, a + T, node::cmpk);
}

int count(const bint& n) {
   int ret = 0;
   for (int i = 0; i < n.m_size; i++)
     ret += g[n.m_data[i]];
   return ret;
 }

void Solve(int m, int n) {
  for (int i = 2; i <= m; i++)
    f[i] = f[i-1] + f[i-2];
  bint fk = f[m];
  for (int i = m; i <= n; i++) {
    f[i] = f[i-1] + f[i-2];
    while (f[i] >= fk) f[i] -= fk;
  }
  for (int i = 1; i <= n; i++)
    dp[i] = dp[i-1] + count(f[i]);
}

void Output() {
  std::sort(a, a + T, node::cmpi);
  for (int i = 0; i < T; i++)
    printf("Case #%d: "i64"\n", i + 1, a[i].ret);
}

//@ Main Function
int main() {
  Init();
  Input();
  for (int i = 0; i < T; i++) {
    if (a[i].k < 3) continue;
    int m = a[i].k;
    int n = m *((m & 1) ? (4) : (2));
    if (!(i && m == a[i-1].k)) Solve(m, n);
    a[i].ret = a[i].n / n * dp[n] + dp[a[i].n % n];
  }
  Output();
  return 0;
}