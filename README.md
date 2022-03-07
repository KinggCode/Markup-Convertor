# Markup-Convertor

# Getting Started with Python Yaml 

Update Pip package before installing the yaml python library 
```sh
pip install --upgrade pip
```

On Windows the recommended command is: 
```sh 
python -m pip install --upgrade pip
```

Install Yaml Python Library to begin  
```sh
pip install pyyaml
```

# Code Structure 
```sh
from dataclasses import dataclass
import yaml 

class MarkupConverter:
    def __init__(self):
        self.inputFile = ""
        self.outputFile = ""
        self.created_at = ""

    def markup_convert(self,outputFile,inputFile):
        data = self.read_markup_file(inputFile)
        result_file = self.write_markup_file(outputFile,data[0],data[1])
        print(result_file)

    # Read Markup Fils
    def read_markup_file(self,inputFile):
        with open(inputFile, "r") as file_descriptor:
            try:
                data = yaml.safe_load(file_descriptor)
                file_type = self.get_file_type(inputFile)
            except yaml.YAMLError as exc:
                print(exc)
        return data , file_type

    # Get File Type 
    def get_file_type(self,inputFile):
        split_data = inputFile.split('.')
        data = split_data[-1]
        return data 

    # Writing Markup files 
    # Default Types : Yaml ,JSON , XML
    def write_markup_file(self,outputFilename,data,type):
        if(type == "json"):
            with open(outputFilename, "w") as file_descriptor:
                yaml.dump(data,file_descriptor)
            return "Successfully Uploaded"

        if(type == "yaml"):
            # code goes here 
            default = "yaml"

        if(type == "xml"):
            # code goes here 
            default = "yaml"

```

# Breakdown
```sh

```

#Use Cases
```sh

```
