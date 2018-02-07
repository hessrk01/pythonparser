from string import ascii_uppercase

import csv
import xlsxwriter as xl
import datetime as dt
import sys

delimiter = ','

workBook = None
workSheet = None

library = None
tables = None

fileName = None



def getLibraryAndTables(csvfilename, delimit):
    
    #global library
    #global tables 
    
    lists = []
    
    libraryOutput = set()
    tableOutput = set()
    
    with open(csvfilename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = delimit)
        for val in reader:
            libraryOutput.add(val[0])
            tableOutput.add(val[1])     
        library = list(libraryOutput)[0]
        tables = list(tableOutput)
        tables.sort()
        
    lists.append(library)
    lists.append(tables)
    return lists
        

def buildWorkbook(library, appenddate=True):
    
    filename = None
    
    if appenddate:
        filename = library + '_' + dt.datetime.now().strftime('%Y%m%d_%H%M') + '.xlsx'
    else:
        filename = library + '.xlsx'
        
    return xl.Workbook(filename)
    
    
def writeHeader(worksheet, header, headerrow):
    
    pass
    
def writeRow(row, rowcount):
    pass
        
def main(csvfilename):
    
    lists = []
    lists = getLibraryAndTables(csvfilename, delimiter)
    library = lists[0]
    tables = lists[1]
    workBook = buildWorkbook(library)
    
    for val in tables:
        workSheet = workBook.add_worksheet(val)    
    
    pass
    
if __name__ == "__main__":
    csvFileName = sys.argv[1]
    main(csvFileName)
    print(library)
    print(tables)


    