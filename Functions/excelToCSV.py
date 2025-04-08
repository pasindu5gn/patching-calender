import pandas

def convertExcelToCSV(sheetName):
    inputFile = "MS Patching Schedule 2025.xlsx"
    outputFile = f"PatchingCSV"
    try:
        df = pandas.read_excel(inputFile, sheetName, engine="openpyxl")
        df.to_csv(outputFile, index=False)
    except Exception as e:
        print(f"ERROR: Failed to conver the file to CSV - {e}. \nExiting.....")
        exit()