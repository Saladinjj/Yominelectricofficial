import openpyxl
import json

file_path = r"C:\Users\Saladin\Desktop\yominelectric-main\Google Merchant Cente2_5r feed - Products source.xlsx"

try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(list(row))
        
    print(json.dumps(data))
except Exception as e:
    print(f"Error: {e}")
