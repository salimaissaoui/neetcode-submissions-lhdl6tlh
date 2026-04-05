class TimeMap:

    def __init__(self):
        #make a dictionary that stores the key, the value and the values timestamp as a tuple
        self.key_to_values = {}


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_values:
            self.key_to_values[key] = []
        self.key_to_values[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_values:
            return ""
        values = self.key_to_values[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return values[right][0] if right >= 0 else ""
    
    
        
