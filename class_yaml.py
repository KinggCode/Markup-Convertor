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





#Create an instance of the MarkupClass
obj = MarkupConverter()

#Read files
#Inputfile = yaml file 
# print(obj.read_markup_file('default.xml'))

## Markup Convert Run
## OutputFile = yaml file  || Inputfile = json file 
obj.markup_convert('default.yaml','test.json')


