/*
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, 
Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t 
will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If 
Teemo attacks again before the poison effect ends, the timer for it is reset, and the 
poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes 
that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

 

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
*/
#include <iostream>
#include <vector>
#include <algorithm>    // for std::min

using std::cout;
using std::endl;
using std::vector;
using std::min;

int findPositionDuration(vector<int>& timeSeries, int duration) {
    if (timeSeries.size() == 0) return 0;
    int total = duration;
    
    for (int i = 1; i < timeSeries.size(); i++) {
        // Get the gap between times:
        int gap = timeSeries[i] - timeSeries[i - 1];
        // add the smaller number to the total: (if overlap, add the gap, else add regular duration)
        total += min(gap, duration);
    }
    return total;
}

int main() {
    vector<int> tS = {1, 4};
    int d1 = 2;
    int totalDuration1 = findPositionDuration(tS, d1);
    cout << "Total Duration: " << totalDuration1 << endl;

    return 0;
}
    
