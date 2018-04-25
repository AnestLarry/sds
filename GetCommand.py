import os,sys
import shutil #del dir

class Command():
    def __init__(self):
        self.tips="""Sort command:
         info > Check > Get > Create > Del > Add > Remove > Database > Databaselist
         """

    def Update(self,commandlist=[]):
        self.__commandlist = commandlist
        self.GetCommand(self.__commandlist)

    def GetCommand(self,key_list=[]):
        if key_list[11]: #info
            print(self.tips)
        elif key_list[10]: #check
            pass
        elif key_list[9]: #get
            pass
        elif key_list[7]: #Create
            self.Create_Path=sys.path[0].replace("\\","/")+"/databases/"+str(key_list[7])
            if os.path.exists(self.Create_Path):
                print("database name is exist!")
            else:
                os.makedirs(self.Create_Path)
                with open(self.Create_Path+"/ReadMe.txt","w",encoding="utf-8") as ReadMeFile:
                    ReadMeFile.write("""Database Created Succeed ,this file can be delete""")
                if os.path.exists(self.Create_Path+"/ReadMe.txt") :
                    print("Database "+str(key_list[7])+" Created Succeed!")
                else:
                    print('Create Error!')


        elif key_list[8]: #Del
            self.Del_Path=sys.path[0]+"/databases/"+key_list[8]
            if os.path.exists(self.Del_Path):
                if input("Warming:\nAre you sure?\nplease keyin y to continue\n")=="y":
                    if input("Last Warming!\nplease keyin database name to continue\n")==key_list[8]:
                        shutil.rmtree('databases/'+key_list[8])
                        print("Delete "+str(key_list[8])+" Succeed!")
            else:
                print("No database named "+key_list[8])
        elif key_list[5] and key_list[2] and key_list[12]: #Add
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path = self.Database_Path + "/" + key_list[12] + ".db"
            if not os.path.exists(self.Database_Path):
                print('No database named'+key_list[2])
                exit()
            elif not os.path.exists(self.Database_List_Path):
                print('Database List '+key_list[12]+' is not exist!')
                exit()
            with open(self.Database_List_Path,'a+',encoding='utf-8') as DatabaseListFile:
                DatabaseListText_List=DatabaseListFile.readlines()
                i=0
                t=""
                while i<len(DatabaseListText_List):
                    DatabaseListText_List[i]=DatabaseListText_List[i].split('   ')
                    i+=1
                for t in DatabaseListText_List:
                    pass
                    #if t[0]==key_list[5]:


        elif key_list[6]: #Remove
            pass
        elif key_list[2] and key_list[3]: #Adddatabaselist
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path=self.Database_Path+"/"+key_list[3]+".db"
            if not os.path.exists(self.Database_Path):
                print('No database named'+key_list[2])
                exit()
            elif os.path.exists(self.Database_List_Path):
                print('Database List is exist!')
                exit()
            else:
                with open(self.Database_List_Path,"w",encoding="utf-8"):
                    print("DatabaseList create succeed!")
        elif key_list[2] and key_list[4]: #Removedatabaselist
            self.Database_Path=sys.path[0]+"/databases/"+key_list[2]
            self.Database_List_Path = self.Database_Path + "/" + key_list[4] + ".db"
            if not os.path.exists(self.Database_Path):
                print('No database named'+key_list[2])
                exit()
            elif not os.path.exists(self.Database_List_Path):
                print('Database List is not exist!')
                exit()
            else:
                if input("Warming:\nAre you sure?\nplease keyin y to continue\n")=="y":
                    try:
                        os.remove(self.Database_List_Path)
                        print("Succeed!")
                    except:
                        print("Error!")


    def result(self):
        pass