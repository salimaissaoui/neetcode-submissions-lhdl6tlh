class Solution:
    def carFleet(self, target, position, speed):
        if not position:
            return 0

        pairs = list(sorted(zip(position, speed), reverse=True))
        fleets = 1
        i = 1

        while i < len(pairs):
            pos_ahead, spd_ahead = pairs[i-1]
            pos_curr, spd_curr = pairs[i]

            if spd_curr < spd_ahead:
                # slower than fleet ahead, can never catch up
                fleets += 1
                i += 1
            elif spd_curr == spd_ahead:
                # same speed — only a new fleet if at different position
                if pos_curr != pos_ahead:
                    fleets += 1
                i += 1
            else:
                x = (pos_ahead - pos_curr) / (spd_curr - spd_ahead)
                meet_pos = spd_curr * x + pos_curr

                if meet_pos <= target:
                    pairs[i] = (pos_ahead, spd_ahead)
                    # don't increment — re-check merged car against next fleet ahead
                else:
                    fleets += 1
                    i += 1

        return fleets