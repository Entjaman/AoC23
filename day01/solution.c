#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
  // Quick argc check
  if (argc != 2) {
    fprintf(stderr, "Only one argument should be passed.");
    exit(EXIT_FAILURE);
  }

  // Start reading file
  FILE* fp = fopen(argv[1], "r");
  char ch;
  if (fp == NULL) {
    perror("Error: ");
    fclose(fp); // Close just in case
    exit(EXIT_FAILURE);
  }
  
  char temp = 0; // temp variable to save first found char
  char num[2]; // saves first two chars found and concats
  int first = 0; // 
  int second = 0;
  int result = 0; // result to be returned
  do {
    ch = fgetc(fp);
    if (ch == '\n') {
      if (!second) { // this means we only found one number in line
        num[1] = num[0];
        result += atoi(num);
      } else {
        result += atoi(num);
      }
      first = 0;
      second = 0;
      printf("first %c and second %c\n", num[0], num[1]);
      continue;
    }
    if (isdigit(ch)) {
      if (!first) {
        num[0] = ch;
        first = 1;
      } else {
        second = 1;
        num[1] = ch;
      }
    }
  } while (ch != EOF);

  fclose(fp);
  printf("The sum is: %d\n", result);

  return EXIT_SUCCESS;
}
