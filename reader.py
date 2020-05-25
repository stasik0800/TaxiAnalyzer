import os,re,sys
import tasks
import data


class FileManager:
    _type ='.csv'

    @staticmethod
    def checkPath(path_in):
        if  not  os.path.exists(path_in):
            print('provide currect path. \n program stopped...')
            sys.exit()

    @staticmethod
    def __checkFileFormat(path_in):
        FileManager.checkPath(path_in)
        if FileManager._type not in path_in:
            print('Wrong file , pass CSV format.\n program stopped...')
            sys.exit()

    @staticmethod
    def getTblName(path_in):
        'Rules for permissible table names'
        FileManager.__checkFileFormat(path_in)
        s = os.path.basename(path_in).replace(FileManager._type,'')
        return re.sub(r'[^\w]', '', s)



class LookupTbl:
    path = data.dataPath
    tblName = FileManager.getTblName(path)
    query_clean = """delete from {0}  where Zone is null or service_zone is null;""".format(tblName)

    @staticmethod
    def execPreLoad(session):
        session.appendCsv2Tbl(LookupTbl.path, LookupTbl.tblName)
        session.execute(LookupTbl.query_clean)


def outFiles(path_out,session,tbls):
    for question,task in tasks.operations.items():
        fileName = task['name']+FileManager._type
        sqlCmd = task['query'].format(**tbls)

        path = os.path.join(path_out, fileName)
        session.tbl2Csv(path,sqlCmd)
        print('files created --> ',path)



