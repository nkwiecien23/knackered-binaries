#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
   setuid(0);
   if (argc > 1) {
       char cmd[30];
       strcpy(cmd, "/usr/bin/zpasswd ");
       strcat(cmd, argv[1]);
       system(cmd);
   } else {
       system("/usr/bin/zpasswd");
   }
   return 0;
}
