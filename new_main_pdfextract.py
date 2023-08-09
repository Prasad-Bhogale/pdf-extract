from tika import parser
import re
import os
import pathlib

BASE_DIR = os.path.join(pathlib.Path(__file__).parent.resolve(), "resume")

def handle(BASE_DIR):
    for current_file in os.listdir(BASE_DIR):
        file_to_process = os.path.join(BASE_DIR, current_file)
        content = parser.from_file(file_to_process)
        content_main= str(content["content"]) if "content" in content.keys() else ""
        
        x = re.search(r"^[A-Z].*\..*",content_main,re.MULTILINE)
        print("name: ",x)
        y = re.search(r"\S+@\S+",content_main,re.MULTILINE)
        print("email: ",y)
        
        

handle(BASE_DIR)
