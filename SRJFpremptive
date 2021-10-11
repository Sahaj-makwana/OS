#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

typedef struct proccess
{
	float at,bt,ct,ta,wt,btt;
	string pro_id;

}Schedule; 

bool compare(Schedule a,Schedule b)
{
	return a.at<b.at;
}
bool compare2(Schedule a,Schedule b)
{
	return a.bt<b.bt;

int main()
{
	Schedule pro[10];
	int n,i,j,pcom;
cout<<"Enter the number of Process::";
	cin>>n;

	cout<<"Enter the Process id arrival time burst time :::";

	for(i=0;i<n;i++)
	{
		cin>>pro[i].pro_id;
		cin>>pro[i].at;
		cin>>pro[i].bt;
		pro[i].btt=pro[i].bt;
	}

	sort(pro,pro+n,compare);
	i=0;
	pcom=0; 
	while(pcom<n)
	{
		for(j=0;j<n;j++)
		{
			if(pro[j].at>i)
			break;
		}

		sort(pro,pro+j,compare2);
if(j>0)
		{

			for(j=0;j<n;j++)
			{
				if(pro[j].bt!=0)
				break;
			}
			if(pro[j].at>i)

			{
				i=pro[j].at;

			}
			pro[j].ct=i+1;
			pro[j].bt--;
		}
		i++;
		pcom=0;
		for(j=0;j<n;j++)
		{
			if(pro[j].bt==0)
			pcom++;
		}
	}

	cout<<"ProID\tAtime\tBtime\tCtime\tTtime\tWtime\n";

	float total_wt=0,total_tat=0;

	for(i=0;i<n;i++)
	{
		pro[i].ta=pro[i].ct-pro[i].at;
		pro[i].wt=pro[i].ta-pro[i].btt;

		total_wt = total_wt + pro[i].wt;
		total_tat = total_tat + pro[i].ta;
			cout<<pro[i].pro_id<<"\t"<<pro[i].at<<"\t"<<pro[i].btt<<"\t"<<pro[i].ct<<"\t"<<pro[i].ta<<"\t"<<pro[i].wt;
		cout<<endl;
	}	
	
	
	cout << "\nAVERAGE WAITING TIME = "
		<< (float)total_wt / (float)n;
	cout << "\nAVERAGE TURN AROUND TIME = "
		<< (float)total_tat / (float)n;
	cout<<endl;
	
	return 0;
}
