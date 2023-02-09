"""
This file gets the 25th option. (back to one name only)
"""
import os
import csv
import pandas as pd
from datetime import date
from pandas import read_csv
from functools import reduce
from itertools import groupby, count

FILE_NAMES = []
PHOTO = "https://american-autographs.com/toimages//{}.jpg|"
VIDEO =  '{}_{}_'
sku_list = []
sku_letters = "RPR"
name_list = []
product_list_length = 0

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

date1 = _date()

def write_list_to_csv_column(files, csv_folder_path):
    d = dict({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'stock':files[3],
                'photos':files[4],
                'column f':files[5],
                'column g':files[6],
                'name':files[7]})
    pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items()])).to_csv(os.path.join(csv_folder_path,'RP porn REG.csv'),index=False)

    print("csv written...")

def col_f(colData, names, inventory_csv_path):
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    colData = read_csv(inventory_csv_path)
    ret_list = ["" for _ in names]
    col_G = colData[data1[6]].tolist() # inventory numbers col
    col_H = colData[data1[7]].tolist() # names columns
    col_I = colData[data1[8]].tolist() # sku columns

    # remove the doubles from list 
    particular_names = reduce(lambda re, x: re+[x] if x not in re else re, names, [])
    names_in_inventory_col_H_with_index = []
    for name in particular_names:

        # Matching the names and getting their index
        for index,lower_col_H in enumerate(col_H):
            if (name.lower() != lower_col_H.lower() 
                and col_I[index].lower() != sku_letters.lower() 
                and name not in names_in_inventory_col_H_with_index):
                names_in_inventory_col_H_with_index.append([name,col_G[index]])
    
    # removing duplicates of the non match.
    res = []
    temp_for_storing_non_dul = []
    for index, val in enumerate(names_in_inventory_col_H_with_index):
            if val[0] not in temp_for_storing_non_dul:
                temp_for_storing_non_dul.append(val[0])
                res.append(val)

    # preparing return list
    if not res:
        return ret_list
    else:
        for j in res:
            ret_list[(j[1])-1] = 24 # type: ignore
            ret_list[j[1]] = 24 # type: ignore
        return ret_list

def col_g(colData, names, inventory_csv_path):
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    colData = read_csv(inventory_csv_path)
    ret_list = ["" for _ in names]
    col_G = colData[data1[6]].tolist() # inventory numbers col
    col_H = colData[data1[7]].tolist() # names columns
    col_I = colData[data1[8]].tolist() # sku columns

    # remove the doubles from list 
    particular_names = reduce(lambda re, x: re+[x] if x not in re else re, names, [])
    names_in_inventory_col_H_with_index = []
    for name in particular_names:

        # Matching the names and getting their index
        for index,lower_col_H in enumerate(col_H):
            if (name.lower() == lower_col_H.lower() 
                and col_I[index].lower() == sku_letters.lower() 
                and name not in names_in_inventory_col_H_with_index):
                names_in_inventory_col_H_with_index.append([name,col_G[index]])

    # Getting random numbers to use for non matches
    non_present_numbers_in_col_G = []
    for i in range(1, max(col_G)+10):
        if i not in col_G:
            non_present_numbers_in_col_G.append(i)

    # Creating the return list by checking the matches and non matches
    if len(names_in_inventory_col_H_with_index) == 0:
        names_in_inventory_col_H_with_index = [[names[0],non_present_numbers_in_col_G[0]]]
        non_present_numbers_in_col_G.remove(non_present_numbers_in_col_G[0])
    for index,name in enumerate(names):
        number = 0
        for i in names_in_inventory_col_H_with_index:
            if name == i[0]:
                ret_list[index] = i[1]
            else:
                another_number = 0
                current_name = names[index]
                while current_name == name:
                    try:
                        current_name = names[index + another_number]
                        ret_list[index + another_number ] = non_present_numbers_in_col_G[number]
                        another_number += 1
                    except:
                        break
                # number += 1

    return (ret_list)

def option_25(FILE_NAMES, csv_folder_path, inventory_csv_path):
    colData = read_csv(inventory_csv_path) # read inventory
    product_list  = []
    price = []
    column_f = []
    stock = []
    photo = []

    product_name = "{} {} autographed Model RP 8x10 Photo RP{}"

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPR"
        sku_list.append(sku)

         # price
        price.append(9.99)

        # sale price
        stock.append(1)

        # photo list
        photo.append(PHOTO.format(i))

        # name list
        name_list.append((First_name+" "+Last_name))
    
    global product_list_length
    product_list_length = int(len(product_list))
    column_f = col_f(colData, name_list, inventory_csv_path=inventory_csv_path)
    column_g = col_g(colData, name_list, inventory_csv_path=inventory_csv_path)
    # column_f_2 = new_col_f(colData, name_list, inventory_csv_path=inventory_csv_path)

    write_list_to_csv_column([product_list, sku_list, price, stock, photo, column_f, column_g, name_list], csv_folder_path=csv_folder_path)

def option_25_3rd_csv(FILE_NAMES, inventory_csv_path):
    column_a = []
    column_b = []
    sku_2 = []
    colData = read_csv(inventory_csv_path) # read inventory
    column_f = col_f(colData, name_list, inventory_csv_path=inventory_csv_path)
    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # getting sku
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPR"
        sku_2.append(sku)

        # column a
        column_a.append('')

    for i in range(product_list_length):
        if column_f[i] == 24:
            try:
                column_b.append(sku_2[i])
            except:
                column_b.append("")
        else:
            column_b.append("")

    return [column_b[:product_list_length], column_a]
