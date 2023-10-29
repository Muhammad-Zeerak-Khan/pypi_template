import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s %(levelname)s]: %(message)s"

    
    )

while True:
    project_name = input("Enter the project name: ")
    if project_name != "":
        break

logging.info(f"Creating project by the name : {project_name}")

# List of files
list_of_file = [
    f"src/{project_name}/__init__.py",

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at {filedir} for file {filename}")

    if not(os.path.exists(Path(filepath))) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file : {filename} at path {filepath}")    
    else:
        logging.info(f"File is already present at : {filepath}")        

