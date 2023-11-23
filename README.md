# CellTower_Task
This is the completion of a task to code the allocation of frequencies to towers based on their longitude and latitude values

## Steps to use
This program is very simple and easy to use. In the following steps i will explain how to use this program and how it works
1. Download the TaskV3 python file and install all relevant addons needed to run the program(Recommend VSCode)
2. Download the tower_data text file and make sure it is in the same directory as your python file as it will not work otherwise.
3. Replace the data in the text file with your own set of value. Keep in mind that the format of the data in the text file should remain the same(A,LONGITUDE,LATITUDE).

##How the code works
1. The code imports all relevant modules needed for the execution of the code. The matplotlib is used to graphically display our results.
2. A class for celltowers and frequency allocater is made to store all relvant data for later use. As well as constructors.
3. Functions are created by means of object oriented creation to ensure uniqueness.
4. There is also functions to calculate the distance between the towers and one to allocate frequencies to each tower based on the distance between those towers. NO tower that is right next to each other will have the same frequency as there should at least be one tower between them that has a different frequency.
5. At this point in the code color are assigned to each unique freuency using nx.coloring.
6. Then the code displays the relevant results of allocation of frequencies in the terminal through use of the display allocation function.
7. The tower locations are plotted on the graph and then the graph is displayed.
8. At the read_tower_data function we read the data from the relevant text file before all other code is executed and assign them to the relevant variables.
9. Lastly is the Main. This is where all the functions are called to be executed in the relevant order to ensure that the code does the task required.

### Output results
![Hello](Results.png)
### Graph Displaying results
This graph displays the results of the frequency allocation program by assigning colors to each frequency and plotting the towers on a grid according to their location. This graph also further shows the accuracy of the program and how the allocation works.
![alt text](Graph.png)

# This code is open to imporvement. If you need any assistance contact me by means of markus01.erasmus@gmail.com
