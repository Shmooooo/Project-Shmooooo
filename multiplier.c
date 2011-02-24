#include <stdio.h>

int multiplier(int a, int b)
{
	int p;
	p = a * b;
	return p;
}

void main()
{
	int r;
	r = multiplier(10, 20);
	printf("The product is: %d", r);
}
