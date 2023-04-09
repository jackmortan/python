# import os

# folder_path = "/Users/shahajisargar/Desktop/output"

# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# import datetime
# now = datetime.datetime.now()
# filename = now.strftime("%Y-%m-%d_%H-%M-%S")


# # Save the data to the file in the folder
# data = "your data here"
# filepath = os.path.join(folder_path, filename + ".txt")
# with open(filepath, "w") as f:
#     f.write(data)

# print("Data saved to", filepath)

import os
import datetime

# Set the path of the folder where you want to save the data
folder_path = "/Users/shahajisargar/Desktop/output"

# Create the folder if it doesn't already exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Generate a filename based on the current date and time
now = datetime.datetime.now()
filename =   "data.txt"

# Save the data to the file in the folder
data = "your data here"
filepath = os.path.join(folder_path, filename)
with open(filepath, "w") as f:
    f.write(data)

# Delete the previous file with the same filename
if os.path.exists(os.path.join(folder_path, filename[:-4])):
    os.remove(os.path.join(folder_path, filename[:-4]))

print("Data saved to", filepath)
