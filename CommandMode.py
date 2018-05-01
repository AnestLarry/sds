import os,sys
import shutil #del dir

class Command():
    def __init__(self):
        self.tips="""Sort command:
         info > Get or Check > Create or Del > Add or Remove or Update > AddDatabaseList or RemoveDatabaaseList > sort
         """

    def Update(self,commandlist=[]):
        self.__commandlist = commandlist
        try:
            self.GetCommand(self.__commandlist)
        except IOError:
            print(IOError)

    def GetCommand(self,key_list=[]):
        if key_list[11]: #info
            print(self.tips)

        elif key_list[9] and key_list[2] and key_list[12] or \
                key_list[10] and key_list[2] and key_list[12] : #get or chekc
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path = self.Database_Path + "/" + key_list[12] + ".db"
            if not os.path.exists(self.Database_Path):
                print('No database named '+key_list[2])
                exit()
            elif not os.path.exists(self.Database_List_Path):
                print('Database List '+key_list[12]+' is not exist!')
                exit()
            with open(self.Database_List_Path,'r',encoding='utf-8') as DatabaseListFile:
                DatabaseListText_List=DatabaseListFile.readlines()
                for i in range(len(DatabaseListText_List)):
                    DatabaseListText_List[i]=DatabaseListText_List[i].strip().split('\t')
                DatabaseListText_Dict=dict(DatabaseListText_List)

            if key_list[9]:
                if key_list[9] in DatabaseListText_Dict.keys():
                    print(DatabaseListText_Dict[key_list[9]])
                else:
                    print("No Var named " + key_list[9])
            elif key_list[10]:
                if key_list[9] in DatabaseListText_Dict.keys():
                    print("True")
                else:
                    print("False")


        elif key_list[7] or key_list[8]: #Create or Del
            self.Create_Path=sys.path[0].replace("\\","/")+"/databases/"+str(key_list[7])
            if os.path.exists(self.Create_Path):
                if key_list[7]:
                    print("database name is exist!")
                elif key_list[8]:
                    if input("Warming:\nAre you sure?\nplease keyin y to continue\n") == "y":
                        if input("Last Warming!\nplease keyin database name to continue\n") == key_list[8]:
                            shutil.rmtree('databases/' + key_list[8])
                            print("Delete " + str(key_list[8]) + " Succeed!")
            else:
                if key_list[7]:
                    os.makedirs(self.Create_Path)
                    with open(self.Create_Path+"/ReadMe.txt","w",encoding="utf-8") as ReadMeFile:
                        ReadMeFile.write("""Database Created Succeed ,this file can be delete""")
                    if os.path.exists(self.Create_Path+"/ReadMe.txt") :
                        print("Database "+str(key_list[7])+" Created Succeed!")
                    else:
                        print('Create Error!')
                elif key_list[8]:
                    print("No database named " + key_list[8])


        elif key_list[5] and key_list[2] and key_list[12] or \
                key_list[6] and key_list[2] and key_list[12] or \
                key_list[13] and key_list[2] and key_list[12] : #Add or Remove or Update
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path = self.Database_Path + "/" + key_list[12] + ".db"
            if not os.path.exists(self.Database_Path):
                print('No database named '+key_list[2])
                exit()
            elif not os.path.exists(self.Database_List_Path):
                print('Database List '+key_list[12]+' is not exist!')
                exit()
            with open(self.Database_List_Path,'r',encoding='utf-8') as DatabaseListFile:
                DatabaseListText_List=DatabaseListFile.readlines()
                for i in range(len(DatabaseListText_List)):
                    DatabaseListText_List[i]=DatabaseListText_List[i].strip().split('\t')
                DatabaseListText_Dict=dict(DatabaseListText_List)
            if key_list[5]:
                if key_list[5][0] in DatabaseListText_Dict.keys():
                    print( key_list[5][0] + " is exist!")
                    exit()
                with open(self.Database_List_Path,'a+',encoding='utf-8') as DatabaseListFile:
                    DatabaseListFile.write(key_list[5][0]+'	'+key_list[5][1]+"\n")
                print(key_list[5][0]+" is add!")
            elif key_list[6]:
                if key_list[6] in DatabaseListText_Dict.keys():
                    del DatabaseListText_Dict[key_list[6]]
                    with open(self.Database_List_Path, 'w', encoding='utf-8') as DatabaseListFile:
                        for DatabaseListTextDict_Key in DatabaseListText_Dict:
                            DatabaseListFile.write(DatabaseListTextDict_Key + "\t" + DatabaseListText_Dict[
                                DatabaseListTextDict_Key] + "\n")
                    print('Delete ' + key_list[6])
                    exit()
                print('No var named ' + key_list[6])
            else :
                if key_list[13][0] in DatabaseListText_Dict.keys():
                    DatabaseListText_Dict[key_list[13][0]] = key_list[13][1]
                else:
                    DatabaseListText_Dict[key_list[13][0]] = key_list[13][1]
                with open(self.Database_List_Path, 'w', encoding='utf-8') as DatabaseListFile:
                    for DatabaseListTextDict_Key in DatabaseListText_Dict:
                        DatabaseListFile.write(
                            DatabaseListTextDict_Key + "\t" + DatabaseListText_Dict[DatabaseListTextDict_Key] + "\n")


        elif key_list[2] and key_list[3] or \
                key_list[2] and key_list[4] : #Adddatabaselist or Removedatabaselist
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path=self.Database_Path+"/"+key_list[3]+".db"
            if not os.path.exists(self.Database_Path):
                print('No database named'+key_list[2])
                exit()
            elif os.path.exists(self.Database_List_Path):
                print('Database List is exist!')
                exit()
            if key_list[3]:
                with open(self.Database_List_Path,"w",encoding="utf-8"):
                    print("DatabaseList create succeed!")
            else:
                if input("Warming:\nAre you sure?\nplease keyin y to continue\n")=="y":
                    try:
                        os.remove(self.Database_List_Path)
                        print("Succeed!")
                    except:
                        print("Error!")


        elif key_list[14] and key_list[2] and key_list[12]:#sort
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path = self.Database_Path + "/" + key_list[12] + ".db"
            if not os.path.exists(self.Database_Path):
                print('No database named '+key_list[2])
                exit()
            elif not os.path.exists(self.Database_List_Path):
                print('Database List '+key_list[12]+' is not exist!')
                exit()
            with open(self.Database_List_Path,'r',encoding='utf-8') as DatabaseListFile:
                DatabaseListText_List=DatabaseListFile.readlines()
                DatabaseListText_List.sort()
            with open(self.Database_List_Path, 'w', encoding='utf-8') as DatabaseListFile:
                for i in range(len(DatabaseListText_List)):
                    DatabaseListFile.write(DatabaseListText_List[i])
                print(key_list[12]+'sort Finished')

