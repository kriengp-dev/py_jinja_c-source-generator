#include <stdio.h>

#define PRINT_MSG       {{ print_msg }}


int main() {
    printf("%s\n", PRINT_MSG);

    {{ func_name }}();

    return 0;
}

/**
 * @brief {{ func_brief }}
 */
void {{ func_name }}()
{
    printf("Print desc : {{ func_desc }}\n");
    printf("Print Int : %d\n",{{ func_int }});
}