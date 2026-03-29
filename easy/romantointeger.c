#include <stdio.h>

int mapper(char a) {
    int values[] = {1, 5, 10, 50, 100, 500, 1000};
    char chars[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    int index = -1;

    for (int i = 0; i < 7; i++) {
        if (a == chars[i]) {
            index = i;
            break;
        }
    }

    return values[index];

}

int romanToInt(char* s) {
    int i = 0;
    int ans = 0;
    int cur = 0;
    int next = 0;

    while (s[i] != '\0') {
        cur = mapper(s[i]);

        if (s[i+1] == '\0') {
            next = cur;
        }
        
        else {
            next = mapper(s[i+1]);
        }

        if (next > cur) {
            ans = ans + (next - cur);
            i++;
        }

        else {
            ans = ans + cur;
        }

        i++;
    }

    return ans;
}