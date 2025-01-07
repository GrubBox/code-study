// Remove a string from the text provided
//
#include<stdio.h>
#include<string.h>

int main(void) {
	char string[] = "Courses!";
	char to_remove ='s'; 
	int length = strlen(string);
	int i = 0;

	while(i < length) {
		if (string[i] == to_remove) break;
		i++;
	}

	while (i<length) {
		string[i] = string[i+1];
		i++;
	}

	printf("%s\n", string);
	return 0;
}
