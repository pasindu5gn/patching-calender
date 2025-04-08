
import csv
from tabulate import tabulate
from Functions.Ticket import createSubTask
from Functions.excelToCSV import convertExcelToCSV

def printCalender(parentIssueKey):
    try:
        with open("PatchingCSV", 'r') as PatchingSchedule:
            PatchingScheduleCSV = csv.reader(PatchingSchedule)
            
            automaticPatching = []
            manualPatching = []
            
            for line in PatchingScheduleCSV:
                if line[5]=="Manual Patching":
                    manualPatching.append(line)
                    createSubTask(parentIssueKey, line[6], line[7])
                elif line[5]=="Automatic Patching":
                    automaticPatching.append(line)
                else:
                    print(f'WARNING: Unkown patching type - {line[5]} for {line[7]}')
            
                
            print("\n Automatic Patching\n")        
            tableData = [[line[6], line[7]] for line in automaticPatching]
            headers = ["Time", "Server Name"]
            print(tabulate(tableData, headers=headers, tablefmt="grid"))
            
            print("\n Manual Patching\n")        
            tableData = [[line[6], line[7]] for line in manualPatching]
            headers = ["Time", "Server Name"]
            print(tabulate(tableData, headers=headers, tablefmt="grid"))
            
    except Exception as e:
        print(f"ERROR: Failed to create subtasks - {e}")
            
parentIssueKey = input("Please enter the partent ticket ID - ")
sheetName = input("Please enter the sheet name of the patching schedule - ")
print("INFO: Converting the excel file to CSV.")
convertExcelToCSV(sheetName)
print("INFO: Creating subtasks on parent ticket.")
printCalender(parentIssueKey)