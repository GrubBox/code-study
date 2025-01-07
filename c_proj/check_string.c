#include<stdio.h>
#include<string.h>
#include<stdbool.h>

bool check_equals(char *str1, char *str2)

int main(void)
{
	char str1[] = "ABCD";
	char str2[] = "ABCD";
 string_equals(str1, str2);
 return 0;
}

bool string_equals(char * s1, char * s2)
{
  if (*s1 != *s2) return false;
	else if (*s1 == '\0') return true;
	return string_equals(s1 + 1, s2 + 1);

	return strcmp(s1, s2) == 0;

}
