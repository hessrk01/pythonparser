from string import ascii_uppercase

import csv
import xlsxwriter as xl
import datetime as dt
import mmap

csvFileName = 'BCJTABLES.csv'
delimiter = ','

class Excel:
    
    fileName = None
    fileExtension = 'xlsx'
    workBook = None
    workSheet = None
    
    
    def __init__(self, filename, appenddate=True):
        
        self.fileName = filename
        
        if appenddate:
            self.fileName = filename + '_' + dt.datetime.now().strftime('%Y%m%d_%H%M')
        self.fileName = self.fileName + '.' + self.fileExtension
        self.workBook = xl.Workbook(self.fileName)
    
    def writeHeader(self, header, headerRow):
        self.workSheet = self.workBook.add_worksheet()
        
        for index, elem in enumerate(header):
            self.workSheet.write(ascii_uppercase[index] + str(headerRow), header[index])          

    def writeRow(self, row, rowCount):
        pass

    def writebook(self):
        self.workBook.close()

class CSVFile:
    
    reader = None
    library = None
    tables = None
    lines = None
    
    def __init__(self, filename, delimiter):
        
        with open(filename) as csvfile:
            #self.reader = csv.reader(csvfile, delimiter)
            lines=list(csvfile)
            print(lines[0][4])
            #self.getLibraryAndTables()
   
    
    def getReader(self):
        pass
        
    def getLibraryAndTables(self):
        libraryOutput = set()
        tableOutput = set()
        for val in self.reader:
            libraryOutput.add(val[0])
            tableOutput.add(val[1])     
        self.library = list(libraryOutput)[0]
        self.tables = list(tableOutput)
        
print(delimiter)
csvFile = CSVFile(csvFileName, delimiter)
print(csvFile.tables)
'''
excelFile = Excel('BCJDTAPRD')
excelFile.writeHeader(['Library', 'Table', 'Column', 'Column Name', 'Data Type], 1)
excelFile.writebook()
'''