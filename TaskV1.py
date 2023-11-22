import math

class CellTower:
    def __init__(self, id, longitude, latitude):
        self.ID = id
        self.Longitude = longitude
        self.Latitude = latitude
        self.Frequency = 0

class FrequencyAllocator:
    MinFrequency = 110
    MaxFrequency = 115

    def __init__(self, towers):
        self.Towers = towers

    def allocate_frequencies(self):
        # Simple allocation: Assign frequencies sequentially and reset when max is reached
        current_frequency = FrequencyAllocator.MinFrequency
        for tower in self.Towers:
            tower.Frequency = current_frequency
            current_frequency += 1
            if current_frequency > FrequencyAllocator.MaxFrequency:
                current_frequency = FrequencyAllocator.MinFrequency

    # Placeholder method for calculating distance between two towers
    # Implement a proper distance calculation based on coordinates
    @staticmethod
    def calculate_distance(tower1, tower2):
        return math.sqrt((tower1.Longitude - tower2.Longitude) ** 2 + (tower1.Latitude - tower2.Latitude) ** 2)

    def display_allocations(self):
        for tower in self.Towers:
            print(f"Cell Tower {tower.ID}: Frequency {tower.Frequency}")

if __name__ == "__main__":
    towers = [
        # Example towers - replace with your actual data
        CellTower("A", -0.03098,51.53657),
        CellTower("B",  -0.02554, 51.53833),
        CellTower("C", -0.02448, 51.53721),
        CellTower("D", -0.02415, 51.5445),
        CellTower("E", -0.02277, 51.54439),
        CellTower("F", -0.02204, 51.54735),
        CellTower("G", -0.02201, 51.54739),
        
        # Add more towers as needed
    ]

    allocator = FrequencyAllocator(towers)
    allocator.allocate_frequencies()
    allocator.display_allocations()
