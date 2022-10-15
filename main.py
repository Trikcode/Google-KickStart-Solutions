# Ada works as a Software Engineer at Google, and needs to get approval for her new project. In order to get an approval, she needs to meet with at least K of N Tech Leads.

# Ada has access to the calendars of all N Tech Leads. For each Tech Lead, Ada can see all their scheduled meetings. The timeline in this problem can be viewed as D consecutive hours, and all meetings are in [0,D] hours range, with both ends being integer numbers. Scheduled meetings, even for the same person, can overlap (people are notorious for this at Google!).

# Ada needs to schedule an X-hour-long meeting in the interval of [0,D] hours, with both ends being integer numbers as well. At least K of N Tech Leads should be present for the whole meeting, that is their calendar should be completely free for the entire meeting duration.

# Unfortunately, it might be the case that it is already impossible to find a slot to schedule such an X-hour-long meeting. In that case, Ada will need to persuade some Tech Leads to cancel their existing meetings.

# What is the minimum number of scheduled meetings that need to be canceled so that Ada can meet with at least K Tech Leads?

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.

# The first line of each test case contains four integers N, K, X, D. N represents the number of Tech Leads, K is the minimum number of Tech Leads Ada needs to meet, X is the length of the meeting that needs to be set up, and D is the upper bound of the [0,D] hour range representing the timeline of the problem — no meeting can end after D.

# The second line of each test case contains an integer M, representing the number of scheduled meetings.

# M lines follow. The i-th of these contains three integer numbers Pi, Li, and Ri. These numbers represent that a Tech Lead Pi has a scheduled meeting between the hours Li and Ri, not including the endpoints (that is, the meeting can be seen as an (Li,Ri) interval).

# Note that all M meetings in the test case are independent, even if some of them have the same starting and ending time.

# Output
# For each test case, output one line containing Case x: y, where x is the test case number (starting from 1) and y is the minimum number of scheduled meetings that needs to be canceled so that Ada can schedule an X-hour-long meeting with at least K Tech Leads.

# Note on the Time Format
# The timeline of this problem can be seen as an [0,D] interval — that is, D consecutive hours, where D can be bigger than 24.

# A meeting in the interval (L,R) means the meeting starts at the beginning of the L-th hour, and ends at the beginning of the R-th hour, covering the whole time period in between, without any gaps (i.e. the interval is continuous). Endpoints are not included in an (L,R) interval. For Tech Leads attending Ada's scheduled meeting, Ada's new meeting can border some of their other non-canceled meetings — that is, it can start right when another meeting ends, or end right when another meeting starts, or both. A Tech Lead cannot attend Ada's meeting if they have any other non-canceled meetings overlapping with Ada's meeting at any point.

# Limits
# Time limit: 40 seconds.
# Memory limit: 1 GB.
# 1≤T≤100.
# 1≤Pi≤N, for all i.
# 0≤Li < Ri≤D, for all i.
#
# Test Set 1
# 1≤X≤D≤8.
# 1≤K≤N≤10.
# 0≤M≤20.
#
# Test Set 2
# 1≤X≤D≤105.
# 1≤K≤N≤105.
# 0≤M≤105

# Sample
# 3
# 3 2 2 6
# 5
# 1 3 5
# 2 1 3
# 2 2 6
# 3 0 1
# 3 3 6
# 3 3 2 6
# 5
# 1 3 5
# 2 1 3
# 2 2 6
# 3 0 1
# 3 3 6
# 3 2 3 6
# 5
# 1 3 5
# 2 1 3
# 2 2 6
# 3 0 1
# 3 3 6

# Case #1: 0
# Case #2: 2
# Case #3: 1

# In Sample Case #1, Ada needs to schedule a two-hour-long meeting with at least two Tech Leads. She can schedule such a meeting between hours 1 and 3 with Tech Leads #1 and #3. In this case, no existing meetings need to be canceled.

# In Sample Case #2, Ada needs to schedule a two-hour-long meeting with all three Tech Leads. She can schedule such a meeting in the interval [0,2], which will require meetings 2 and 4 to be canceled. Another option is to schedule a meeting in the interval [1,3]. Both options require two meetings to be canceled, which is the minimum number possible.

# In Sample Case #3, Ada needs to schedule a three-hour-long meeting with at least two Tech Leads. She can schedule this meeting in the interval [0,3], and meet with Tech Leads #1 and #3. This will require meeting 4 to be canceled, and this is the optimal solution here.

# solution

def main():
    T = int(input())
    for i in range(T):
        N, K, X, D = map(int, input().split())
        M = int(input())
        meetings = []
        for j in range(M):
            P, L, R = map(int, input().split())
            meetings.append((P, L, R))
        print('Case #{}: {}'.format(i+1, solve(N, K, X, D, meetings)))


def solve(N, K, X, D, meetings):
    if K == N:
        return 0
    if X > D:
        return -1
    meetings.sort(key=lambda x: x[1])
    meetings.sort(key=lambda x: x[0])
    for i in range(len(meetings)):
        if meetings[i][1] - meetings[i][0] >= X:
            return 0
    for i in range(len(meetings)):
        for j in range(i+1, len(meetings)):
            if meetings[i][0] == meetings[j][0] and meetings[i][1] == meetings[j][1]:
                continue
            if meetings[i][0] <= meetings[j][0] and meetings[i][1] >= meetings[j][1]:
                return 1
            if meetings[i][0] >= meetings[j][0] and meetings[i][1] <= meetings[j][1]:
                return 1
            if meetings[i][0] <= meetings[j][0] and meetings[i][1] >= meetings[j][0]:
                return 1
            if meetings[i][0] <= meetings[j][1] and meetings[i][1] >= meetings[j][1]:
                return 1
    return 2


if __name__ == '__main__':
    main()
