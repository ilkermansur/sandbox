import pandas as pd

# load xlsx file
excel_file = "vlan_mapping.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(excel_file, sheet_name = sheet_name)
data_dict = df.to_dict()
list_data_keys = list(list(data_dict.values())[1])

for vlan in list_data_keys:
    config_str = 'conf t'+'\n'+f'interface vlan {vlan}' + '\n'
    print (config_str)

