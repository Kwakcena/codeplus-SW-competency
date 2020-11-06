#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
  string str = "rhkrgudwh";
  string str1 = "12345";

  string cmp_str1 = "abcde";
  string cmp_str2 = "abcze";

  // string 클래스의 변수를 출력하려면 cout은 그냥 쓰면 되지만,
  // cstdio 라이브러리를 이용한 printf로 출력할 때는 c_str() 를 붙여야 한다.
  cout << str << endl;
  printf("%s\n", str.c_str());

  // string 클래스의 변수 맨 뒤 문자를 반환함.
  printf("%c\n", str.back());

  // str의 사이즈를 반환함.
  printf("%lu\n", str.size());
  printf("%lu\n", str.length());

  // 5번째 index 부터 1개 반환
  cout << str.substr(5, 1) << endl;

  // 5번째 index 부터 2개를 str1으로 대체
  cout << str.replace(5, 2, str1) << endl;

  // cmp_str1 이 cmp_str2 보다 사전순으로 작으면 음수, 크면 양수. 같으면 0
  cout << cmp_str1.compare(cmp_str2) << endl;
  return 0;

}