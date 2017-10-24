#include<iostream>
#include<vector>
#include<string>
using namespace std;

string longestCommonPrefix(vector<string>& strs)
{
	if(strs.size() == 0)
		return "";
	int count = 0;
	string s = strs[0];
	while(true)
	{
		for(int i = 1; i < strs.size(); i++)
		{
			if(count == strs[i].size())
				return strs[0].substr(0,count - 1);
			else
			{
				if (strs[i][count] != s[count])
					return strs[0].substr(0, count - 1);
			}
		}
		count ++;
	}
	
}

int main()
{
	vector<string> a = {"123","1234","12345"};
	cout<<longestCommonPrefix(a);
}