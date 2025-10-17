import json
filepath = r"D:\redi_a25_python\Watch_list_Project"

def load():
    flag = False
    try:
        with open(filepath + r"\data.json",'r') as file_csv:
            local_data = json.load(file_csv)
            flag = True
    except:
        flag = False

    if flag:
        return local_data
    else:
        return None

def escape_csv_field(s):
    s = str(s).replace('"', '""')  # escape inner double quotes
    return f'"{s}"'  # wrap whole string in double quotes

def export_CSV(data):
    with open(filepath + r"\data.csv",'w') as file_csv:
        wtr_str = "Sr.no,Title,Genres,Rating,Summary,Watched,Review out of 5\n"
        file_csv.write(wtr_str)
        for key, value in data.items():
            wtr_str = (
                        escape_csv_field(key) + "," +
                        escape_csv_field(value['Title']) + "," +
                        escape_csv_field('/'.join(value['Genres'])) + "," +
                        escape_csv_field(value['Rating']) + "," +
                        escape_csv_field(value['Summary']) + "," +
                        escape_csv_field(value['Watched']) + "," +
                        escape_csv_field(value['Review']) + "\n"
                    )
            file_csv.write(wtr_str)

def save(data):
    json_str = json.dumps(data, indent=4)
    with open(filepath + r"\data.json",'w') as file_csv:
        file_csv.write(json_str)



