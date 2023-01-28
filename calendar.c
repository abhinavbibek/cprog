#include <stdio.h>
#include <time.h>

int main() {
    time_t currentTime;
    struct tm *localTime;

    time(&currentTime); // Get the current time
    localTime = localtime(&currentTime); // Convert the current time to the local time

    int year = localTime->tm_year + 1900;
    int month = localTime->tm_mon + 1;
    int day = localTime->tm_mday;

    printf("Today's date is %d/%d/%d\n", month, day, year);

    return 0;
}
