#include <iostream>
using namespace std;

int main(void)
{
    int a,b;
   
    cin>>a>>b;
    if(a>=1 && b<=10000)
    {
    cout<<a+b<<endl;
    cout<<a-b<<endl;
    cout<<a*b<<endl;
    cout<<a/b<<endl;
    cout<<a%b<<endl;
    }
  
    return 0;
}