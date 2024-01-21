import os 
import json
import pandas as pd
import mysql.connector

# agg-trans

path1="C:/Users/ELCOT/Desktop/Srini/pulse/data/aggregated/transaction/country/india/state/"

agg_trans_list= os.listdir(path1)

Columns1={"States":[],"Years":[],"Quarters":[],"Transaction_Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in agg_trans_list:
    state_path= path1 + state +"/"
    agg_year_list=os.listdir(state_path)
    
    for year in agg_year_list:
        year_path= state_path + year + "/"
        agg_file_list=os.listdir(year_path)

        for file in agg_file_list:
            file_path = year_path + file
            data=open(file_path)      #data=open(file_path,"r")

            A = json.load(data)

            for i in A["data"]["transactionData"]:
                Name=i["name"]
                Count=i["paymentInstruments"][0]["count"]
                Amount=i["paymentInstruments"][0]["amount"]
                Columns1["States"].append(state)
                Columns1["Years"].append(year)
                Columns1["Quarters"].append(int(file.strip(".json")))
                Columns1["Transaction_Type"].append(Name)
                Columns1["Transaction_Count"].append(Count)
                Columns1["Transaction_Amount"].append(Amount)

agg_trans=pd.DataFrame(Columns1)

agg_trans["States"] = agg_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
agg_trans["States"] = agg_trans["States"].str.replace("-"," ")
agg_trans["States"] = agg_trans["States"].str.title()
agg_trans['States'] = agg_trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#agg-User

path2="C:/Users/ELCOT/Desktop/Srini/pulse/data/aggregated/user/country/india/state/"

agg_user_list= os.listdir(path2)

Columns2={"States":[],"Years":[],"Quarters":[],"Brands":[],"Transaction_Count":[],"Percentage":[]}

for state in agg_user_list:
    state_path= path2 + state +"/"
    agg_year_list=os.listdir(state_path)
    
    for year in agg_year_list:
        year_path= state_path + year + "/"
        agg_file_list=os.listdir(year_path)

        for file in agg_file_list:
            file_path = year_path + file
            data=open(file_path)      #data=open(file_path,"r")

            B = json.load(data)
            
            try:

                for i in B["data"]["usersByDevice"]:
                    Brand=i["brand"]
                    Count=i["count"]
                    Percentage=i["percentage"]
                    Columns2["States"].append(state)
                    Columns2["Years"].append(year)
                    Columns2["Quarters"].append(int(file.strip(".json")))
                    Columns2["Brands"].append(Brand)
                    Columns2["Transaction_Count"].append(Count)
                    Columns2["Percentage"].append(Percentage)
            except:
                pass

agg_user=pd.DataFrame(Columns2)

agg_user["States"] = agg_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
agg_user["States"] = agg_user["States"].str.replace("-"," ")
agg_user["States"] = agg_user["States"].str.title()
agg_user['States'] = agg_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#map-trans

path3="C:/Users/ELCOT/Desktop/Srini/pulse/data/map/transaction/hover/country/india/state/"

map_trans_list=os.listdir(path3)

Columns3={"States":[],"Years":[],"Quarters":[],"Districts":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in map_trans_list:
    state_path= path3 + state +"/"
    agg_year_list=os.listdir(state_path)
    
    for year in agg_year_list:
        year_path= state_path + year + "/"
        agg_file_list=os.listdir(year_path)

        for file in agg_file_list:
            file_path = year_path + file
            data=open(file_path)      #data=open(file_path,"r")

            C = json.load(data)

            for i in C["data"]["hoverDataList"]:
                Name=i["name"]
                Count=i["metric"][0]["count"]
                Amount=i["metric"][0]["amount"]
                Columns3["States"].append(state)
                Columns3["Years"].append(year)
                Columns3["Quarters"].append(int(file.strip(".json")))
                Columns3["Districts"].append(Name)
                Columns3["Transaction_Count"].append(Count)
                Columns3["Transaction_Amount"].append(Amount)

map_trans=pd.DataFrame(Columns3)

map_trans["States"] = map_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_trans["States"] = map_trans["States"].str.replace("-"," ")
map_trans["States"] = map_trans["States"].str.title()
map_trans['States'] = map_trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#map_user

path4="C:/Users/ELCOT/Desktop/Srini/pulse/data/map/user/hover/country/india/state/"

map_user_list=os.listdir(path4)

Columns4={"States":[],"Years":[],"Quarters":[],"Districts":[],"Registered_Users":[],"App_Opens":[]}

for state in map_user_list:
    state_path= path4 + state +"/"
    agg_year_list=os.listdir(state_path)
    
    for year in agg_year_list:
        year_path= state_path + year + "/"
        agg_file_list=os.listdir(year_path)

        for file in agg_file_list:
            file_path = year_path + file
            data=open(file_path)      #data=open(file_path,"r")

            D = json.load(data)

            for i in D["data"]["hoverData"].items():
                Name=i[0]
                Users=i[1]["registeredUsers"]
                AppOpens=i[1]["appOpens"]
                Columns4["States"].append(state)
                Columns4["Years"].append(year)
                Columns4["Quarters"].append(int(file.strip(".json")))
                Columns4["Districts"].append(Name)
                Columns4["Registered_Users"].append(Users)
                Columns4["App_Opens"].append(AppOpens)

map_user=pd.DataFrame(Columns4)

map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user["States"] = map_user["States"].str.replace("-"," ")
map_user["States"] = map_user["States"].str.title()
map_user['States'] = map_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#top_trans

path5="C:/Users/ELCOT/Desktop/Srini/pulse/data/top/transaction/country/india/state/"

top_trans_list=os.listdir(path5)

Columns5={"States":[],"Years":[],"Quarters":[],"Pincodes":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in top_trans_list:
    state_path= path5 + state +"/"
    agg_year_list=os.listdir(state_path)
    
    for year in agg_year_list:
        year_path= state_path + year + "/"
        agg_file_list=os.listdir(year_path)

        for file in agg_file_list:
            file_path = year_path + file
            data=open(file_path)      #data=open(file_path,"r")

            E = json.load(data)

            for i in E["data"]["pincodes"]:
                Name=i["entityName"]
                Count=i["metric"]["count"]
                Amount=i["metric"]["amount"]
                Columns5["States"].append(state)
                Columns5["Years"].append(year)
                Columns5["Quarters"].append(int(file.strip(".json")))
                Columns5["Pincodes"].append(Name)
                Columns5["Transaction_Count"].append(Count)
                Columns5["Transaction_Amount"].append(Amount)

top_trans=pd.DataFrame(Columns5)

top_trans["States"] = top_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_trans["States"] = top_trans["States"].str.replace("-"," ")
top_trans["States"] = top_trans["States"].str.title()
top_trans['States'] = top_trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#top_user

path6="C:/Users/ELCOT/Desktop/Srini/pulse/data/top/user/country/india/state/"

top_user_list=os.listdir(path6)

Columns6={"States":[],"Years":[],"Quarters":[],"Pincodes":[],"Registered_Users":[]}

for state in top_user_list:
    state_path= path6 + state +"/"
    agg_year_list=os.listdir(state_path)
    
    for year in agg_year_list:
        year_path= state_path + year + "/"
        agg_file_list=os.listdir(year_path)

        for file in agg_file_list:
            file_path = year_path + file
            data=open(file_path)      #data=open(file_path,"r")

            F = json.load(data)

            for i in F["data"]["pincodes"]:
                Name=i["name"]
                Users=i["registeredUsers"]
                Columns6["States"].append(state)
                Columns6["Years"].append(year)
                Columns6["Quarters"].append(int(file.strip(".json")))
                Columns6["Pincodes"].append(Name)
                Columns6["Registered_Users"].append(Users)

top_user=pd.DataFrame(Columns6)

top_user["States"] = top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_user["States"] = top_user["States"].str.replace("-"," ")
top_user["States"] = top_user["States"].str.title()
top_user['States'] = top_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



# Table Creation

mydb = mysql.connector.connect(host="localhost",
            user="root",
            password="",
            database = "Phonepe_Data",
            port = "3306"
            )
mycursor = mydb.cursor()

# agg_trans Table

create_query1 = '''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarters int,
                                                                      Transaction_Type varchar(50),
                                                                      Transaction_Count bigint,
                                                                      Transaction_Amount bigint
                                                                      )'''
mycursor.execute(create_query1)
mydb.commit()

for index,row in agg_trans.iterrows():
    insert_query1 = '''INSERT INTO aggregated_transaction (States, Years, Quarters, Transaction_Type, Transaction_Count, Transaction_Amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarters"],
              row["Transaction_Type"],
              row["Transaction_Count"],
              row["Transaction_Amount"]
              )
    mycursor.execute(insert_query1,values)
    mydb.commit()

# agg_user Table

create_query2 = '''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quarters int,
                                                                Brands varchar(50),
                                                                Transaction_Count bigint,
                                                                Percentage float)'''
mycursor.execute(create_query2)
mydb.commit()

for index,row in agg_user.iterrows():
    insert_query2 = '''INSERT INTO aggregated_user (States,Years,Quarters,Brands,Transaction_Count,Percentage)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarters"],
              row["Brands"],
              row["Transaction_Count"],
              row["Percentage"])
    mycursor.execute(insert_query2,values)
    mydb.commit()

# map_trans Table

create_query3 = '''CREATE TABLE if not exists map_transaction (States varchar(50),
                                                                Years int,
                                                                Quarters int,
                                                                Districts varchar(50),
                                                                Transaction_Count bigint,
                                                                Transaction_Amount float)'''
mycursor.execute(create_query3)
mydb.commit()

for index,row in map_trans.iterrows():
        insert_query3 = ''' INSERT INTO map_Transaction (States, Years, Quarters, Districts, Transaction_Count, Transaction_Amount)
            VALUES (%s, %s, %s, %s, %s, %s) '''
        values = (
            row['States'],
            row['Years'],
            row['Quarters'],
            row['Districts'],
            row['Transaction_Count'],
            row['Transaction_Amount']
        )
        mycursor.execute(insert_query3,values)
        mydb.commit() 

# map_user Table

create_query4 = '''CREATE TABLE if not exists map_user (States varchar(50),
                                                        Years int,
                                                        Quarters int,
                                                        Districts varchar(50),
                                                        Registered_Users bigint,
                                                        App_Opens bigint)'''
mycursor.execute(create_query4)
mydb.commit()

for index,row in map_user.iterrows():
    insert_query4 = '''INSERT INTO map_user (States, Years, Quarters, Districts, Registered_Users, App_Opens)
                        values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarters"],
              row["Districts"],
              row["Registered_Users"],
              row["App_Opens"])
    mycursor.execute(insert_query4,values)
    mydb.commit()

# top_trans Table

create_query5 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarters int,
                                                                Pincodes int,
                                                                Transaction_Count bigint,
                                                                Transaction_Amount bigint)'''
mycursor.execute(create_query5)
mydb.commit()

for index,row in top_trans.iterrows():
    insert_query5 = '''INSERT INTO top_transaction (States, Years, Quarters, Pincodes, Transaction_Count, Transaction_Amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarters"],
              row["Pincodes"],
              row["Transaction_Count"],
              row["Transaction_Amount"])
    mycursor.execute(insert_query5,values)
    mydb.commit()

# top_user Table

create_query6 = '''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quarters int,
                                                        Pincodes int,
                                                        Registered_Users bigint
                                                        )'''
mycursor.execute(create_query6)
mydb.commit()

for index,row in top_user.iterrows():
    insert_query6 = '''INSERT INTO top_user (States, Years, Quarters, Pincodes, Registered_Users)
                                            values(%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarters"],
              row["Pincodes"],
              row["Registered_Users"])
    mycursor.execute(insert_query6,values)
    mydb.commit()

