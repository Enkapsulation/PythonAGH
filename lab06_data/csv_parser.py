#!/usr/bin/python3
import csv
import enquiries

'''

'''
def read_file_csv(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        RecordDict = {}
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            RecordDict[line_count] = {}
            RecordDict[line_count]["ip_addr"] = row["ip_addr"]
            RecordDict[line_count]["attack_type"] = row["attack_type"]
            RecordDict[line_count]["counter"] = row["counter"]
            RecordDict[line_count]["entropy"] = row["entropy"]
            line_count += 1
        return RecordDict, line_count

'''

'''
def save_csv(filename, dictionary):
    with open(filename, mode='w') as csv_file:
        fieldnames = ['ip_addr', 'attack_type', 'counter', 'entropy']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for element in dictionary:
            writer.writerow({'ip_addr': dictionary[element]["ip_addr"], 'attack_type': dictionary[element]["attack_type"], 'counter': dictionary[element]["counter"], 'entropy': dictionary[element]["entropy"] })

'''

'''
def add_row_csv(dictionary, place):
    counter = sum(len(v) for v in dictionary.itervalues())

'''

'''
def delete_record_csv(dictionary, record_to_delete):
    i = 1
    while dictionary[i]["ip_addr"] is not None:
        if record_to_delete == dictionary[i]["ip_addr"]:
            del dictionary[i]
            break

        i += 1
'''

'''
def show_actual_content_csv(dictionary):
    print("ip_addr,attack_type,counter,entropy")
    
    for element in dictionary:
        print(f'{dictionary[element]["ip_addr"]},    {dictionary[element]["attack_type"]},    {dictionary[element]["counter"]},   {dictionary[element]["entropy"]}')

'''

'''
def menu():
    options = ['Add record', 'Delete record', 'Show csv content', 'Save file', 'Quit']
    choice = enquiries.choose('Choose one of these options: ', options)

    return choice



def test():
    file = "MaliciousIPAddr.csv"
    modifying_csv, line_counter = read_file_csv(file)
    show_actual_content_csv(modifying_csv)
    
    while 1:
        option = menu()
        if "Add record" == option:
            pass
        elif "Delete record" == option:
            ip_address = input("Enter the ip adress: ")
            try:
                delete_record_csv(modifying_csv, ip_address)
                show_actual_content_csv(modifying_csv)
            except:
                print("Can not find record try again")      
        elif "Show csv content" == option:
            pass
        elif "Save file" == option:
            save_csv(file, modifying_csv)
        elif "Quit" == option:
            break

if __name__ == "__main__":
   test()