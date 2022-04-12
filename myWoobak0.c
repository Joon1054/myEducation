#include <iostream>

long long int memo[10000001] = { 0 };   //메모
long long int max = 0;   //최대 길이
int locate = 0;   //최대 길이의 수

//최대 길이및 최대 길이 수 구하는 함수
long long int mymax(long long int a, long long int b, int c) {
   if (a > b) {
      locate = c;
      return a;
   }
   else return b;
}

//우박수 구하는 재귀함수
long long int recur(long long int a) {
   if (a == 1) return 1;

   //천만이 넘는 큰 수라면(메모배열넘음) 메모안함
   if (a > 10000000) {
      if (a % 2 == 0) return recur(a / 2) + 1;
      else return recur(a * 3 + 1) + 1;
   }

   //메모가 되어 있다면 함수 호출 말고 메모값 리턴
   if (memo[a] != 0) return memo[a];

   //메모, 재귀 호출
   else {
      if (a % 2 == 0) return memo[a] = recur(a / 2) + 1;
      else return memo[a] = recur(a * 3 + 1) + 1;
   }
}

int main() {

   int a, b;
   std::cin >> a >> b;

   //주어진 범위 호출
   while (a < b + 1) {
      long long int temp = recur(a);
      max = mymax(temp, max, a);
      ++a;
   }

   printf("%d %lld\n", locate, max);

   return 0;
}
