#from asyncore import write
from msilib.schema import File
import os, sys, re, copy, datetime
import getpass
from ast import parse
import argparse






default_type_set = (".cc", ".h", ".cpp", ".py", ".sh")
default_annotation_type_set = {
  "//":(".cc", ".h", ".cpp"),
  "#":(".py")
  }

class CreateFile:
  def __init__(self):
    self._file_name = ""
    self._path = ""
    self._file_type = ""
    self._full_path = ""
    self._annotation_type = ""

    
    self._has_type = False

    

  def setFileName(self, file_name):
    self._file_name = file_name

    if not self._has_type:
      idx = self._file_name.rfind('.')
      if idx != -1:
        self._file_type = self._file_name[idx:]
  
  def setFilePath(self, file_path):
    self._path = file_path

  def setFileType(self, file_type):
    self._file_type = file_type
    self._has_type = True

  def setAnnotationType(self):
    if self._file_type:
      for writing_type, type_set in default_annotation_type_set.items():
        if self._file_type in type_set:
          self._annotation_type = writing_type
  

  def createOneFile(self):
    #check input param
    if self._file_name == "":
      print("no File Input")
      return 
    
    if self._path == "":
      print("check path")
      return 

    if self._has_type:
      self._file_name = self._file_name + self._file_type

    self._full_path = os.path.join(self._path, self._file_name)
    print(self._full_path)

    with open(self._full_path, "w") as f:
      #writeContent
      self.writeFileBegin(f)
      self.writeFileContent(f)
    

  def writeFileBegin(self, FILE):
    FILE.write("%s -*- encoding : utf-8 -*-\n" % self._annotation_type)
    FILE.write("\n")
    FILE.write("%s============================================================================\n" % self._annotation_type)
    FILE.write("%s Copyright (c) 2022, All Right Reserved\n" % self._annotation_type)
    FILE.write("\n")
    FILE.write("%s file:      %s\n" % (self._annotation_type, self._file_name))
    FILE.write("%s author:    %s\n" % (self._annotation_type, format(getpass.getuser())))
    FILE.write("%s time:    %s\n" % (self._annotation_type, format(datetime.datetime.now())))
    FILE.write("%s============================================================================\n\n" % self._annotation_type)
    

  def writeFileContent(self, FILE):
    if self._file_type == ".h":
      FILE.write("#include <fstream>\n")
      FILE.write("#include <stdint.h>\n")
      FILE.write("#include <cstddef>\n")
      FILE.write("#include <vector>\n")
      FILE.write("#include <assert.h>\n")
  
    elif self._file_type == ".py":
      FILE.write("import os, sys, re\n")
      
    

  def writeFileEnd(self, FILE):
    pass
    
    
    
    
    
'''
def writeFileHead(self) :
  OutputFile.write("%s -*- encoding : utf-8 -*-\n" % Annotation)
  OutputFile.write("\n")
  OutputFile.write("%s============================================================================\n" % Annotation)
  OutputFile.write("%s Copyright (c) 2022, All Right Reserved, X_Lab\n" % Annotation)
  OutputFile.write("\n")
  OutputFile.write("%s file:      %s.%s\n" % (Annotation, FileName, FileType))
  OutputFile.write("%s author:    {}\n".format(getpass.getuser()) % Annotation)
  OutputFile.write("%s time:    {}\n".format(datetime.datetime.now()) % Annotation)
  OutputFile.write("%s purpose:   XXXXX\n" % Annotation)
  OutputFile.write("%s revision history:\n" % Annotation)
  def createFile(self):
    pass

def writePythonFileContent(FileName, FileType, Annotation) :
  full_file_name = FileName + "." + FileType
  output_file = open(full_file_name, mode="w")
  writeFileHead(output_file, FileName, FileType, Annotation)
  output_file.write("#============================================================================\n")
  output_file.write("import os\n")
  output_file.write("import sys\n")
  output_file.write("import re\n")
  
  output_file.write("\n\n")
  output_file.write("def %s():\n" % FileName)
  output_file.write("  pass\n")

  output_file.write("\n\n")
  
  output_file.write("if __name__ == '__main__':\n")
  output_file.write("  pass\n")

  output_file.close()

def writeCFileContent (FileName, FileType, Annotation) :
  full_file_name = FileName + "." + FileType
  output_file = open(full_file_name, mode="w")
  writeFileHead(output_file, FileName, FileType, Annotation)                                                          
  output_file.write("//============================================================================\n")
  output_file.write("\n")
  output_file.write("#ifndef %s\n" % ("XXXXXXXXXXXXXXXXXXXXXX" if FileName == "" else FileName.upper() + "_H_"))
  output_file.write("#define %s\n" % ("XXXXXXXXXXXXXXXXXXXXXX" if FileName == "" else FileName.upper() + "_H_"))
  output_file.write("\n")
  
  output_file.write("#include <%s.h>" % FileName)
  output_file.write("\n")
  output_file.write("namespace X_Lab {\n")
  output_file.write("\n")

  output_file.write("\n")
  output_file.write("\n")
  output_file.write("} // namespace X_Lab\n")
  output_file.write("\n")
  output_file.write("#endif\n")

  output_file.close()

def writeHFileContent(FileName, FileType, Annotation) :
  full_file_name = FileName + "." + FileType
  output_file = open(full_file_name, mode="w")
  writeFileHead(output_file, FileName, FileType, Annotation)
  output_file.write("\n")
  
  output_file.write("#ifndef %s\n" % ("XXXXXXXXXXXXXXXXXXXXXX" if FileName == "" else FileName.upper() + "_H_"))
  output_file.write("#define %s\n" % ("XXXXXXXXXXXXXXXXXXXXXX" if FileName == "" else FileName.upper() + "_H_"))
  output_file.write("\n")
  output_file.write("#include <fstream>\n")
  output_file.write("#include <stdint.h>\n")
  output_file.write("#include <cstddef>\n")
  output_file.write("#include <vector>\n")
  output_file.write("#include <assert.h>\n")
  output_file.write("#include \"common/common_utility.h\"\n")
  output_file.write("namespace X_Lab {\n")
  output_file.write("\n")

  output_file.write("\n")
  output_file.write("\n")
  output_file.write("} // namespace X_Lab\n")
  output_file.write("\n")
  output_file.write("#endif\n")

  output_file.close()


def writeFileHead(OutputFile, FileName, FileType, Annotation) :
  OutputFile.write("%s -*- encoding : utf-8 -*-\n" % Annotation)
  OutputFile.write("\n")
  OutputFile.write("%s============================================================================\n" % Annotation)
  OutputFile.write("%s Copyright (c) 2022, All Right Reserved, X_Lab\n" % Annotation)
  OutputFile.write("\n")
  OutputFile.write("%s file:      %s.%s\n" % (Annotation, FileName, FileType))
  OutputFile.write("%s author:    {}\n".format(getpass.getuser()) % Annotation)
  OutputFile.write("%s time:    {}\n".format(datetime.datetime.now()) % Annotation)
  OutputFile.write("%s purpose:   XXXXX\n" % Annotation)
  OutputFile.write("%s revision history:\n" % Annotation)

   ''' 


if __name__ == "__main__" :
  file_name = "test.h"
  path = "F:\Python\create_template"

  newFile = CreateFile()


  newFile.setFileName(file_name)
  newFile.setFilePath(path)
  newFile.setAnnotationType()
  newFile.createOneFile()

        