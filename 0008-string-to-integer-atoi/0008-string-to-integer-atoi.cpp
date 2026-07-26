class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();

        // Skip leading spaces
        while (i < n && s[i] == ' ')
            i++;

        // Check sign
        int sign = 1;
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            if (s[i] == '-')
                sign = -1;
            i++;
        }

        long long num = 0;

        // Read digits
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';

            // Overflow check
            if (num > (LLONG_MAX - digit) / 10)
                return sign == 1 ? INT_MAX : INT_MIN;

            num = num * 10 + digit;

            if (sign * num > INT_MAX)
                return INT_MAX;

            if (sign * num < INT_MIN)
                return INT_MIN;

            i++;
        }

        return sign * num;
    }
};