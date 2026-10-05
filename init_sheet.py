import gspread

try:
    gc = gspread.service_account(filename='convertionalai-d8da9e4d43dd.json')
    sh = gc.open_by_key('1NAu0Syl4AYeGpgmOps32l6Tkc2AZcHED4SoFcqJM5wk')
    
    # Try to open or create the CarUI_Results worksheet
    try:
        worksheet = sh.worksheet('CarUI_Results')
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title='CarUI_Results', rows="1000", cols="20")
        
    # Also initialize Sheet1 just in case
    try:
        sheet1 = sh.sheet1
        if not sheet1.get_all_values():
            sheet1.append_row(['Test ID', 'Batch', 'Timestamp', 'Model', 'Scenario', 'Latency', 'Status', 'Action Chain', 'Total Steps'])
    except Exception as e:
        pass

    # Clear and insert row titles
    worksheet.clear()
    headers = ['Test ID', 'Batch', 'Timestamp', 'Model', 'Scenario', 'Latency', 'Status', 'Action Chain', 'Total Steps']
    worksheet.append_row(headers)
    print("Successfully initialized spreadsheet with row titles (headers).")
except Exception as e:
    print(f"Error initializing spreadsheet: {e}")
