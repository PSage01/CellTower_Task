import math
import matplotlib.pyplot as plt

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

    # Placeholder method for calculating distance between two towers
    @staticmethod
    def calculate_distance(tower1, tower2):
        return math.sqrt((tower1.Longitude - tower2.Longitude) ** 2 + (tower1.Latitude - tower2.Latitude) ** 2)

    def allocate_frequencies(self):
        used_frequencies = set()
        for tower in self.Towers:
            available_frequencies = set(range(FrequencyAllocator.MinFrequency, FrequencyAllocator.MaxFrequency + 1))
            for other_tower in self.Towers:
                if tower != other_tower:
                    distance = self.calculate_distance(tower, other_tower)
                    if distance < 0.01:  
                        if other_tower.Frequency in available_frequencies:
                            available_frequencies.remove(other_tower.Frequency)
            if available_frequencies:
                tower.Frequency = min(available_frequencies)
                used_frequencies.add(tower.Frequency)
            else:
                print(f"Unable to allocate a frequency for Tower {tower.ID}.")
        return used_frequencies

    def display_allocations(self):
        for tower in self.Towers:
            print(f"Cell Tower {tower.ID}: Frequency {tower.Frequency}")

    def plot_tower_locations(self):
        longitude = [tower.Longitude for tower in self.Towers]
        latitude = [tower.Latitude for tower in self.Towers]
        tower_names = [tower.ID for tower in self.Towers]
        frequencies = [tower.Frequency for tower in self.Towers]
        unique_colors = range(len(self.Towers))
        
        # Create the scatter plot with unique colors
        plt.figure(figsize=(8, 8))
        scatter = plt.scatter(longitude, latitude, c=unique_colors, cmap='viridis', s=100)
        
        # Add tower names as labels
        for i, name in enumerate(tower_names):
            plt.annotate(name, (longitude[i], latitude[i]), textcoords='offset points', xytext=(0, 10), ha='center')
        
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Cell Tower Locations')
        
        # Adjust the x-axis limits to shift the graph to the left
        plt.xlim(min(longitude) - 0.005, max(longitude) + 0.005)
        
        plt.grid(True)
        plt.show()

def read_tower_data_from_file(filename):
    towers = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                tower_id, longitude, latitude = parts
                towers.append(CellTower(tower_id, float(longitude), float(latitude)))
    return towers

if __name__ == "__main__":
    filename = "tower_data.txt"  
    towers = read_tower_data_from_file(filename)

    allocator = FrequencyAllocator(towers)
    used_frequencies = allocator.allocate_frequencies()
    allocator.display_allocations()
    print(f"Used Frequencies: {used_frequencies}")

    # Plot the tower locations with tower names as labels (without legend)
    allocator.plot_tower_locations()
