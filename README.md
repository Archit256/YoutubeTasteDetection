# YoutubeTasteDetection

The main python program is videograph.py


Required - NetworkX installation

------Important --------

Drawing the graph for the whole dataset is quite hard. If you want to draw and plot it - 
Do the following - 

split -l 500 scores.csv 
This will split the file into lines of 500 each.

Change the line - 
with open('scores.csv', 'rb') as csvfile:
to 
with open('xaj', 'rb') as csvfile:
and run the program again.
