class TimeMap:

    def __init__(self):

        # Dictionary:
        # key -> list of [value, timestamp]
        #
        # Example:
        # {
        #   "foo": [["bar",1], ["bar2",4], ["bar3",7]]
        # }
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        # If this key hasn't been seen before,
        # create an empty list for it
        if key not in self.keyStore:
            self.keyStore[key] = []

        # Add the new [value, timestamp] pair
        # Since timestamps are always increasing,
        # the list stays sorted by timestamp
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        # res stores the best answer found so far.
        # Start with "" in case no valid timestamp exists.
        res = ""

        # Get the list for this key.
        # If the key doesn't exist, use an empty list instead.
        values = self.keyStore.get(key, [])

        # Binary search pointers
        l = 0
        r = len(values) - 1

        # Continue searching while the pointers haven't crossed
        while l <= r:

            # Find the middle index
            m = (l + r) // 2

            # If this timestamp is LESS THAN OR EQUAL TO
            # the one we're searching for...
            if values[m][1] <= timestamp:

                # This is a possible answer.
                # Save its value.
                res = values[m][0]

                # But there might be an even later timestamp
                # that's still <= timestamp, so search RIGHT.
                l = m + 1

            else:
                # Timestamp is too large.
                # Search the LEFT half instead.
                r = m - 1

        # Return the latest valid value found.
        # If none existed, this is just "".
        return res
        
