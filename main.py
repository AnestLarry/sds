import argparse , os ,sys ,shutil ,zipfile ,time
import CommandMode

class sds_Shell:
    def __init__(self):
        self.Setting_Dict=()
        self.__Version=2.0
        self.Get_Shell_Setting_def()
        self.run()

    def Get_Shell_Setting_def(self):
        if os.path.exists("setting.ini"):
            with open("setting.ini", 'r', encoding='utf-8') as SettingFile:
                Setting_List = SettingFile.readlines()
                for i in range(len(Setting_List)):
                    Setting_List[i] = Setting_List[i].strip().split('\t')
            self.Setting_Dict = dict(Setting_List)
            if 'Database' in self.Setting_Dict.keys():
                self.Database_Path=sys.path[0]+"/databases/"+self.Setting_Dict['Database']
            if "DatabaseList" in self.Setting_Dict.keys():
                self.Database_List_Path = self.Database_Path + "/" + self.Setting_Dict["DatabaseList"] + ".db"
        else:
            with open("setting.ini",'w',encoding='utf-8') as Setting_File :
                Setting_File.write("")
            self.Setting_Dict=()

    def run(self):
        print('Into Shell')
        while True:
            self.Command=input("\n").split(' ')
            if self.Command[0] == 'Path':
                self.Database_Path = sys.path[0] + "/databases/" + self.Command[1]
                if os.path.exists(self.Database_Path):
                    self.Setting_Dict["Database"] = self.Command[1]
                    self.Save_Setting_def()
                    self.Database_List_Path=''
                    print('Database checkout : '+self.Command[1])
                else:
                    self.Database_Path=None
                    print('No database named '+self.Command[1])

                self.Database_List_Path = self.Database_Path + "/" + self.Command[2] + ".db"
                if os.path.exists(self.Database_List_Path):
                    self.Setting_Dict["DatabaseList"] = self.Command[2]
                    self.Save_Setting_def()
                    print('DatabaseList checkout : '+self.Command[2])
                else:
                    self.Database_List_Path=None
                    print('No DatabaseList named '+self.Command[2])

            elif self.Command[0] == 'Database':
                self.Database_Path = sys.path[0] + "/databases/" + self.Command[1]
                if os.path.exists(self.Database_Path):
                    self.Setting_Dict["Database"] = self.Command[1]
                    self.Save_Setting_def()
                    self.Database_List_Path=''
                    print('Database checkout : '+self.Command[1])
                else:
                    self.Database_Path=None
                    print('No database named '+self.Command[1])


            elif self.Command[0] == 'Create':
                self.Create_Path = sys.path[0].replace("\\", "/") + "/databases/" + self.Command[1]
                if os.path.exists(self.Create_Path):
                    print("database name is exist!")
                else:
                    os.makedirs(self.Create_Path)
                    with open(self.Create_Path + "/ReadMe.txt", "w", encoding="utf-8") as ReadMeFile:
                        ReadMeFile.write("""Database Created Succeed ,this file can be delete""")
                    if os.path.exists(self.Create_Path + "/ReadMe.txt"):
                        print("Database " + self.Command[1] + " Created Succeed!")
                    else:
                        print('Create Error!')


            elif self.Command[0] == 'Del':
                self.Del_Path = sys.path[0] + "/databases/" +self.Command[1]
                if os.path.exists(self.Del_Path):
                    if input("Warming:\nAre you sure?\nplease keyin y to continue\n") == "y":
                        if input("Last Warming!\nplease keyin database name to continue\n") == self.Command[1]:
                            shutil.rmtree('databases/' + self.Command[1])
                            print("Delete " + self.Command[1] + " Succeed!")
                else:
                    print("No database named " + self.Command[1])


            elif self.Command[0] == 'DatabaseList':
                self.Database_List_Path = self.Database_Path + "/" + self.Command[1] + ".db"
                if os.path.exists(self.Database_List_Path):
                    self.Setting_Dict["DatabaseList"] = self.Command[1]
                    self.Save_Setting_def()
                    print('DatabaseList checkout : '+self.Command[1])
                else:
                    self.Database_List_Path=None
                    print('No DatabaseList named '+self.Command[1])


            elif self.Command[0] == 'AddDatabaseList'or \
                    self.Command[0] == 'RemoveDatabaseList':
                self.Database_List_Path = self.Database_Path + "/" + self.Command[1] + ".db"
                if not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                elif os.path.exists(self.Database_List_Path):
                    print('DatabaseList '+self.Command[1]+' is exist!')
                else:
                    if self.Command[0] == 'AddDatabaseList':
                        with open(self.Database_List_Path, "w", encoding="utf-8"):
                            print("DatabaseList create succeed!")
                    elif self.Command[0] == 'RemoveDatabaseList':
                        if input("Warming:\nAre you sure?\nplease keyin y to continue\n") == "y":
                            try:
                                os.remove(self.Database_List_Path)
                                print("Succeed!")
                            except:
                                print("Error!")


            elif self.Command[0] == 'Add':
                if not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                elif not os.path.exists(self.Database_List_Path):
                    print('Database List ' + self.Database_List_Path + ' is not exist!')
                with open(self.Database_List_Path, 'r', encoding='utf-8') as DatabaseListFile:
                    DatabaseListText_List = DatabaseListFile.readlines()
                    for i in range(len(DatabaseListText_List)):
                        DatabaseListText_List[i] = DatabaseListText_List[i].strip().split('\t')
                    DatabaseListText_Dict = dict(DatabaseListText_List)
                if self.Command[1] in DatabaseListText_Dict.keys():
                    print(self.Command[1] + " is exist!")
                with open(self.Database_List_Path, 'a+', encoding='utf-8') as DatabaseListFile:
                    DatabaseListFile.write(self.Command[1] + '\t' + self.Command[2] + "\n")
                print(self.Command[1] + " is add!")


            elif self.Command[0] == 'Remove':
                if not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                elif not os.path.exists(self.Database_List_Path):
                    print('Database List ' + self.Database_List_Path + ' is not exist!')
                with open(self.Database_List_Path, 'r', encoding='utf-8') as DatabaseListFile:
                    DatabaseListText_List = DatabaseListFile.readlines()
                    for i in range(len(DatabaseListText_List)):
                        DatabaseListText_List[i] = DatabaseListText_List[i].strip().split('\t')
                    DatabaseListText_Dict = dict(DatabaseListText_List)
                if self.Command[1] in DatabaseListText_Dict.keys():
                    del DatabaseListText_Dict[self.Command[1]]
                    with open(self.Database_List_Path, 'w', encoding='utf-8') as DatabaseListFile:
                        for DatabaseListTextDict_Key in DatabaseListText_Dict:
                            DatabaseListFile.write(DatabaseListTextDict_Key + "\t" + DatabaseListText_Dict[
                                DatabaseListTextDict_Key] + "\n")
                    print('Delete ' + self.Command[1])
                else:
                    print('No var named ' + self.Command[1])


            elif self.Command[0] == 'Update':
                if not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                elif not os.path.exists(self.Database_List_Path):
                    print('Database List ' + self.Database_List_Path + ' is not exist!')
                with open(self.Database_List_Path, 'r', encoding='utf-8') as DatabaseListFile:
                    DatabaseListText_List = DatabaseListFile.readlines()
                    for i in range(len(DatabaseListText_List)):
                        DatabaseListText_List[i] = DatabaseListText_List[i].strip().split('\t')
                    DatabaseListText_Dict = dict(DatabaseListText_List)
                if self.Command[1] in DatabaseListText_Dict.keys():
                    DatabaseListText_Dict[self.Command[1]] = self.Command[2]
                else:
                    DatabaseListText_Dict[self.Command[1]] = self.Command[2]
                with open(self.Database_List_Path, 'w', encoding='utf-8') as DatabaseListFile:
                    for DatabaseListTextDict_Key in DatabaseListText_Dict:
                        DatabaseListFile.write(
                            DatabaseListTextDict_Key + "\t" + DatabaseListText_Dict[DatabaseListTextDict_Key] + "\n")


            elif self.Command[0] == 'Get' or self.Command[0] == 'Check':
                if not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                elif not os.path.exists(self.Database_List_Path):
                    print('Database List ' + self.Database_List_Path + ' is not exist!')
                with open(self.Database_List_Path, 'r', encoding='utf-8') as DatabaseListFile:
                    DatabaseListText_List = DatabaseListFile.readlines()
                    for i in range(len(DatabaseListText_List)):
                        DatabaseListText_List[i] = DatabaseListText_List[i].strip().split('\t')
                    DatabaseListText_Dict = dict(DatabaseListText_List)

                if self.Command[0] == 'Get':
                    if self.Command[1] in DatabaseListText_Dict.keys():
                        print(DatabaseListText_Dict[self.Command[1]])
                    else:
                        print("No Var named " + self.Command[1])
                else:
                    if self.Command[1] in DatabaseListText_Dict.keys():
                        if DatabaseListText_Dict[self.Command[1]]==self.Command[2]:
                            print("True")
                        else:
                            print("False")
                    else:
                        print("False")


            elif self.Command[0] == 'sort':
                if not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                elif not os.path.exists(self.Database_List_Path):
                    print('Database List ' + self.Database_List_Path + ' is not exist!')
                with open(self.Database_List_Path, 'r', encoding='utf-8') as DatabaseListFile:
                    DatabaseListText_List = DatabaseListFile.readlines()
                    DatabaseListText_List.sort()
                with open(self.Database_List_Path, 'w', encoding='utf-8') as DatabaseListFile:
                    for i in range(len(DatabaseListText_List)):
                        DatabaseListFile.write(DatabaseListText_List[i])
                    print( self.Database_List_Path + 'sort Finished')


            elif self.Command[0] == 'info':
                print("""Sort command:
         info > Get or Check > Create > Del > Add > Remove > Update > AddDatabaseList or RemoveDatabaaseList > sort
         """)


            elif self.Command[0] == 'status':
                if self.Database_Path:
                    print('Database : '+self.Database_Path)
                if self.Database_List_Path:
                    print('DatabaseList : '+self.Database_List_Path)


            elif self.Command[0] == 'exit' or self.Command[0] == 'quit':
                self.Save_Setting_def()
                exit()


            elif self.Command[0] == 'cls':
                os.system('cls')


            elif self.Command[0] == 'Version':
                print(self.__Version)


            elif self.Command[0] == 'help':
                self.help="""Path DatabaseName DatabaseListName

Database DatabaseName

Create/Del DatabaseName

AddDatabaseList/RemoveDatabaseList DatabaseListName

Add/Remove/Update AddVarName AddVarValue/ RemoveVarName / UpdateVarName UpdateVarValue

Get/Check VarName

info / status / exit / quit / cls / help
                 """
                print(self.help)

            elif self.Command[0] == 'Backup' and self.Command[1]:
                if not os.path.exists("databases/" + self.Command[1]):
                    print("No Database named "+self.Command[1])
                elif not os.path.exists(self.Database_Path):
                    print('No database named ' + self.Database_Path)
                else:
                    backup_zip = zipfile.ZipFile(str(sys.path[0]) + "/"+ self.Command[1] + "_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".zip",
                                                 'w')
                    for folder, subfolders, files in os.walk("databases/" + self.Command[1]):
                        for filename in files:
                            print(str(os.path.relpath(os.path.join(folder, filename))))
                            backup_zip.write(os.path.join(folder, filename), self.Command[1] + "/" + filename,
                                             compress_type=zipfile.ZIP_DEFLATED)
                    backup_zip.close()
                    print(self.Command[1] + 'backup succed')

            elif self.Command[0]=="Restore" and self.Command[1]:
                if os.path.exists(self.Database_Path):
                    print(self.Command[1] + ' Database is exist')
                else:
                    restore_zip = zipfile.ZipFile(self.Command[1], 'r')
                    restore_zip.extractall("databases")
                    restore_zip.close()
                    print("restore succ")

            else:
                print('Error Commmand ',self.Command)


    def Save_Setting_def(self):
        with open("setting.ini",'w',encoding='utf-8') as DatabaseListFile :
            for Setting_Key in self.Setting_Dict:
                DatabaseListFile.write(Setting_Key+"\t"+self.Setting_Dict[Setting_Key]+"\n")

if __name__ == '__main__' :
    fileparser = argparse.ArgumentParser()
    fileparser.add_argument('-Account', default=None, help='your account')
    fileparser.add_argument('-Password', default=None, help='your password')
    fileparser.add_argument('-Database', default="", help='into database name')
    fileparser.add_argument('-DatabaseList', default="", help='into a database list')
    fileparser.add_argument('-AddDatabaseList', default="", help='Database\'s list Name')
    fileparser.add_argument('-RemoveDatabaseList', default="", help='Database\'s list Name')
    fileparser.add_argument('-Add', default=[], nargs=2, help='add var to database before into a database')
    fileparser.add_argument('-Remove', default=[], help='remove var to database before into a database')
    fileparser.add_argument('-Update', default=[], nargs=2, help='Update var to database before into a database')
    fileparser.add_argument('-Create', default="", help='create a database before log in')
    fileparser.add_argument('-Del', default="", help='delete a database before log in')
    fileparser.add_argument('-Get', default="", help='get a var in a database before into a databaselist')
    fileparser.add_argument('-Check', default="", nargs=2,help='check your var ture or false before into a databaselist')
    fileparser.add_argument('-sort', default=False, help='sort the databaselist')
    fileparser.add_argument('-info', default=False, help='true to get command info next')
    fileparser.add_argument('-Backup',default=False,help='backup your database')
    fileparser.add_argument('-Restore',default="",help='restore your database')
    fileparser.add_argument('-Shell', default=False, help='shell mode')

    fileargs = fileparser.parse_args()
    file_args_list = [""] * 18
    try:
        file_args_list[0] = fileargs.Account
        file_args_list[1] = fileargs.Password
        file_args_list[2] = fileargs.Database
        file_args_list[3] = fileargs.AddDatabaseList
        file_args_list[4] = fileargs.RemoveDatabaseList
        file_args_list[5] = fileargs.Add
        file_args_list[6] = fileargs.Remove
        file_args_list[7] = fileargs.Create
        file_args_list[8] = fileargs.Del
        file_args_list[9] = fileargs.Get
        file_args_list[10] = fileargs.Check
        file_args_list[11] = fileargs.info
        file_args_list[12] = fileargs.DatabaseList
        file_args_list[13] = fileargs.Update
        file_args_list[14] = fileargs.sort
        file_args_list[15] = fileargs.Shell
        file_args_list[16] = fileargs.Backup
        file_args_list[17] = fileargs.Restore

    except IOError:
        print(IOError)

    if not file_args_list[15]:
        GetCommand_app = CommandMode.Command()
        GetCommand_app.Update(file_args_list)
        exit()
    else:
        sds_shell = sds_Shell()
