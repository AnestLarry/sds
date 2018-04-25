import argparse
import GetCommand

fileparser = argparse.ArgumentParser()
fileparser.add_argument('-Account',default=None,help='your account')
fileparser.add_argument('-Password',default=None,help='your password')
fileparser.add_argument('-Database',default="",help='into database name')
fileparser.add_argument('-DatabaseList',default="",help='into a database list')
fileparser.add_argument('-AddDatabaseList',default="",help='Database\'s list Name')
fileparser.add_argument('-RemoveDatabaseList',default="",help='Database\'s list Name')
fileparser.add_argument('-Add',default="",help='add var to database before into a database')
fileparser.add_argument('-Remove',default="",help='remove var to database before into a database')
fileparser.add_argument('-Create',default="",help='create a database before log in')
fileparser.add_argument('-Del',default="",help='delete a database before log in')
fileparser.add_argument('-Get',default="",help='get a var in a database before into a databaselist')
fileparser.add_argument('-Check',default="",help='check your var ture or false before into a databaselist')
fileparser.add_argument('-info',default=False,help='true to get command info next')

fileargs = fileparser.parse_args()
file_args_list=[""]*13
try:
    file_args_list[0]=fileargs.Account
    file_args_list[1]=fileargs.Password
    file_args_list[2]=fileargs.Database
    file_args_list[3]=fileargs.AddDatabaseList
    file_args_list[4]=fileargs.RemoveDatabaseList
    file_args_list[5]=fileargs.Add
    file_args_list[6]=fileargs.Remove
    file_args_list[7]=fileargs.Create
    file_args_list[8]=fileargs.Del
    file_args_list[9]=fileargs.Get
    file_args_list[10]=fileargs.Check
    file_args_list[11]=fileargs.info
    file_args_list[12]=fileargs.DatabaseList
except IOError:
    print(IOError)

GetCommand_app=GetCommand.Command()
GetCommand_app.Update(file_args_list)
Command_list=GetCommand_app.result()
