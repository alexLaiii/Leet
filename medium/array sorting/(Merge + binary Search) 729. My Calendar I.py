    """
    A simple calendar that supports non-overlapping bookings using
    a DIY binary search over a start-time–sorted list of intervals.

    Invariant:
        - `self.booked` is always sorted by start time.
        - Intervals are **non-overlapping** and treated as half-open: [start, end).

    Approach:
        - On `book(startTime, endTime)`, perform a binary search on `self.booked`
          to find the insertion index `i = r + 1` (the first interval with
          start >= startTime). Only the immediate neighbors can conflict:
              • left neighbor at index i-1
              • right neighbor at index i
        - Reject if `[startTime, endTime)` overlaps either neighbor; otherwise
          insert at `i`.

    Correctness sketch:
        - Because the list is sorted by start times and already non-overlapping,
          any overlap with `[startTime, endTime)` must involve at most one of the
          two neighbors around the insertion point. Checking these two is sufficient.

    Complexity:
        - Search: O(log n) for the binary search.
        - Insert: O(n) for shifting elements in the Python list.
        - Space: O(n) for stored intervals.

    Example:
        >>> cal = MyCalendar()
        >>> cal.book(10, 20)  # True, calendar: [[10, 20)]
        True
        >>> cal.book(15, 25)  # False, overlaps [10, 20)
        False
        >>> cal.book(20, 30)  # True, touches but doesn't overlap (half-open)
        True
    """

class MyCalendar:

    def __init__(self):
        self.booked = []
        

    def book(self, startTime: int, endTime: int) -> bool:

        """
        Try to add a half-open interval [startTime, endTime) to the calendar.

        Uses a hand-written binary search to locate the insertion point `i = r + 1`,
        then checks only the left and right neighbors for overlap:

            - Front edge (i == 0): reject if endTime > booked[0][0]
            - Back edge  (i == len): reject if startTime < booked[-1][1]
            - Middle (0 < i < len): reject if startTime < booked[i-1][1] or
              endTime > booked[i][0]

        If no overlap is detected, inserts at index `i` and returns True.

        Args:
            startTime: Start time of the new booking (inclusive).
            endTime:   End time of the new booking (exclusive).

        Returns:
            True if the booking was added; False if it overlaps an existing booking.
        """
        if not self.booked:
            self.booked.append([startTime, endTime])
            return True
        else:
            l,r = 0, len(self.booked) - 1
            while l <= r:
                mid = (l + r) // 2
                if self.booked[mid][0] == startTime:
                    return False
                elif self.booked[mid][0] > startTime:
                    r = mid - 1
                else:
                    l = mid + 1
            if r + 1 == 0 and endTime > self.booked[0][0]:
                return False
            elif r + 1 == len(self.booked) and startTime < self.booked[-1][1]:
                return False
            elif r + 1 > 0 and r + 1 < len(self.booked) and (startTime < self.booked[r][1] or endTime > self.booked[r + 1][0]):
                return False
            self.booked.insert(r + 1, [startTime, endTime])
            return True

                
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
