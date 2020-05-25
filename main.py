from connection import MysqlDb as db
import reader
import warnings

warnings.filterwarnings("ignore")

mysql_auth = {'host': '127.0.0.1:3306',  # using local host docker image
              'user': 'root',
              'password': 'stasek123',
              'database': 'stas_db'}

tbls = {}
chucksize = 100000

if "__main__" == __name__:
    session = db(mysql_auth)
    reader.LookupTbl.execPreLoad(session)

    print('please provide location + yellow_tripdata_2018-01.csv')

    path_in = input('provide input csv file : ')
    reader.FileManager.checkPath(path_in)

    path_out = input('provide output dir for files : ')
    reader.FileManager.checkPath(path_out)

    tbls['lookuptbl'] = reader.LookupTbl.tblName
    tbls['uploadedtbl'] = reader.FileManager.getTblName(path_in)

    session.appendCsv2Tbl(path_in, tbls['uploadedtbl'], chunsize=chucksize)
    reader.outFiles(path_out, session, tbls)
