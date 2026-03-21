
class RecentCounter:
    """ 
    Status: COMPLETE
    Ref: https://leetcode.com/problems/number-of-recent-calls/
    Description:
    You have a RecentCounter class which counts the number of recent requests within a certain time frame.

    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns
    the number of requests that has happened in the past 3000 milliseconds (including the new request).
    Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
    It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
    """
    def __init__(self) -> None:
        """Initializes the counter with zero recent requests."""
        self.recent_requests = []

    def ping(self, time_in_milliseconds: int) -> int:
        """ Adds a new request representing the time in milliseconds and returns the number of requests that
        has happened in the past 3000 milliseconds (including the new request).
        """
        self.recent_requests.append(time_in_milliseconds)
        return len([request for request in self.recent_requests if request >= time_in_milliseconds - 3000 and request <= time_in_milliseconds])
