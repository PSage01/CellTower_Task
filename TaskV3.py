
#import the math module to use in this code as it will be used to calculate distance between code
#Import matplotlib which is a module that can graph data as it is used to show the towers on a basic grid with their corresponding frequencies
#Import networkx as nx. This is used to import networkx with an alias it make sure that each tower gets a unique value and that no entry does not have a frequency
#The networkX as nx uses an algorithm to determine if the towers are next to eachother
import math
import matplotlib.pyplot as plt
import networkx as nx

#Cell tower class this is where the instance of a celltower is created with its unique attributes
class CellTower:
    def __init__(self, id, longitude, latitude):
        self.ID = id
        self.Longitude = longitude
        self.Latitude = latitude
        self.Frequency = 0

# Class that asssigns the maximum and minimum frequencies for later use in assignment
class FrequencyAllocator:
    MinFrequency = 110
    MaxFrequency = 115 

    #This Function has an inner part which is the object-oriented code which is the __init__
    #Self is used to reference this class for better coding practise and assigns the value that will be retrieved to towers
    #This whole code makes up a class
    def __init__(self, celltowers):
        self.CellTowers = celltowers

    # Method for calculating distance between towers
    #Make it a static method that dos not change depending on values
    @staticmethod
    #This function does tha calculation through the use of math import and we use the squareroot to use basi pythagoras theorym(No PUN intended on the pyth)
    def calculate_distance(tower1, tower2):
        return math.sqrt((tower1.Longitude - tower2.Longitude) ** 2 + (tower1.Latitude - tower2.Latitude) ** 2)

    #This function allocates frequencies based on their distance. Here the networkx module is used to make sure that each tpwer gets a value
    def allocate_frequencies(self):
        graph = nx.Graph()
        for celltower in self.CellTowers:
            graph.add_node(celltower.ID)

        #This part of the code compares towers that is stored by use of their distance between eachother if they are different
        for tower1 in self.CellTowers:
            for tower2 in self.CellTowers:
                if tower1 != tower2:
                    distance = self.calculate_distance(tower1, tower2)
                    if distance < 0.01:  # Distance threshold between towers
                        graph.add_edge(tower1.ID, tower2.ID)

        # Use graph coloring to allocate color to be able to distinguish them
        coloring = nx.coloring.greedy_color(graph, strategy='largest_first')

        for celltower in self.CellTowers:
            celltower.Frequency = (coloring[celltower.ID] % (self.MaxFrequency - self.MinFrequency + 1)) + self.MinFrequency  
#the rest of this code plots on the graph 
    def display_allocations(self):
        for celltower in self.CellTowers:
            print(f"Cell Tower {celltower.ID}: Frequency {celltower.Frequency}")

    def plot_tower_locations(self):
        longitude = [celltower.Longitude for celltower in self.CellTowers]
        latitude = [celltower.Latitude for celltower in self.CellTowers]
        tower_names = [celltower.ID for celltower in self.CellTowers]
        frequencies = [celltower.Frequency for celltower in self.CellTowers]

        plt.figure(figsize=(8, 8))
        scatter = plt.scatter(longitude, latitude, c=frequencies, cmap='viridis', s=100)
        
        for i, name in enumerate(tower_names):
            plt.annotate(name, (longitude[i], latitude[i]), textcoords='offset points', xytext=(0, 10), ha='center')
        
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Cell Tower Locations')
        
        plt.xlim(min(longitude) - 0.005, max(longitude) + 0.005)
        
        plt.grid(True)
        plt.colorbar(scatter, label='Frequency')
        plt.show()
        
#Read data from textfile to use
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
    allocator.allocate_frequencies()
    allocator.display_allocations()

    # Plot the tower locations with tower names and frequencies
    allocator.plot_tower_locations()
