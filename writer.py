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
    tableOutputDict = {}

    with open(csvfilename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = delimit)
        for val in reader:
            libraryOutput.add(val[0])
            tableOutput.add(val[1])
            tableOutputDict.update({val[1]:val[7]})

        library = list(libraryOutput)[0]
        tables = list(tableOutput)
        tables.sort()
        sorted(tableOutputDict.keys())

    lists.append(library)
    lists.append(tables)
    lists.append(tableOutputDict)
    return lists


def buildWorkbook(library, appenddate=True):

    filename = None

    if appenddate:
        filename = library + '_' + dt.datetime.now().strftime('%Y%m%d_%H%M') + '.xlsx'
    else:
        filename = library + '.xlsx'

    return xl.Workbook(filename)


def writeHeader(worksheet, header, headerrow):
    for index, elem in enumerate(header):
            worksheet.write(ascii_uppercase[index] + str(headerrow), header[index])

def writeRow(worksheet, row, rownumber, width):
    worksheet.write('A' + str(rownumber), row[0])
    worksheet.write('B' + str(rownumber), row[1])
    worksheet.write('C' + str(rownumber), row[2])
    worksheet.write('D' + str(rownumber), row[5])
    worksheet.write('E' + str(rownumber), row[4])

    for n, i in enumerate(width):
        worksheet.set_column(n,n,i+3)

def setColumnWidth(maxSizeList, lengthList):
    for n, x in enumerate(maxSizeList):
        if x < lengthList[n]:
            maxSizeList[n] = lengthList[n]
    return maxSizeList

def createTitleSheet(library, tables, workBook):
    row=0
    col=0
    colSize=0
    col2Size=0

    workSheet = workBook.add_worksheet('Title')
    workSheet.set_first_sheet()

    workSheet.write(row, col, 'Library: %s - Data tables' % (library))
    workSheet.set_column(row,col,len(library)+20)
    row += 2

    workSheet.write(row, col, 'Tables:')

    col += 1

    for k,v in tables.items():

        workSheet.write_url(row, col, 'internal:%s!A1' %(k), string='%s'%(k))
        colSize = len(k) if colSize < len(k) else colSize
        workSheet.set_column(row,col, colSize+3)
        workSheet.write(row, col+1, v)
        col2Size=len(v) if col2Size < len(v) else col2Size
        workSheet.set_column(row,col+1, col2Size+3)

        row += 1

def main(csvfilename):

    lists = []
    lists = getLibraryAndTables(csvfilename, delimiter)
    library = lists[0]
    tables = lists[1]
    tablesWithNames = lists[2]

    workBook = buildWorkbook(library)

    createTitleSheet(library, tablesWithNames, workBook)

    maxList = []
    header = ['Library', 'Table', 'Column', 'Data Type', 'Column Description']
    length_list = [len(x) for x in header]

    for val in tables:
        workSheet = workBook.add_worksheet(val)
        writeHeader(workSheet, header, '1')

        maxList = length_list

        with open(csvfilename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter = delimiter)
            rownumber = 1
            for row in reader:

                if val == row[1]:
                    newrow = (row[0], row[1], row[2], row[5], row[4])
                   # print('rownumber: %s - val: %s - row: %s', rownumber, val, row[1])
                    rownumber += 1
                    maxColWidth = setColumnWidth(maxList, [len(x) for x in newrow])
                    #print(len(row))
                    writeRow(workSheet, row, rownumber, maxColWidth)


    workBook.close()

if __name__ == "__main__":
    csvFileName = sys.argv[1]
    main(csvFileName)
