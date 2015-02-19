#include <stdio.h>
#include <time.h>
long long fibo(long n){
	long x=0,y=1,temp=0;
	int counter=0;
	for (counter;counter<n;counter++)
	{
		temp=x+y;
		x=y;
		y=temp;
	}
	return temp;
}
int main(void){
	clock_t start,diff;
	start=clock();
	FILE *file ;
	file=fopen("fiboc.txt","w+");
	int counter=0;
	for(counter;counter<1500;counter++){
		fprintf(file, "number%d =%lld\n", counter+1,fibo(counter));
	}
	diff=clock()-start;
	fprintf(file, "Time is equal=%ld\n",(diff));
	fclose(file);
	return 0;
}