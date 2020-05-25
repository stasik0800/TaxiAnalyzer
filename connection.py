import pandas as pd
from sqlalchemy import create_engine


class MysqlDb:
    def __init__(self,conf):
        self.conf= conf
        self._set_connetion()

    def _set_connetion(self):
        try:
            self.engine = create_engine(self.getConStringMysql)
        except Exception as e:
            raise e

    def getDataFrame(self, query):
        return pd.read_sql(query,self.engine)

    def execute(self,query):
        pd.io.sql.execute(query,con=self.engine)

    def appendCsv2Tbl(self,pathin,tblName,chunsize=None):
        clean = 'drop table if exists {0} ;'.format(tblName)
        self.execute(clean)
        for inx,chunk in enumerate(pd.read_csv(pathin,sep=',',chunksize=chunsize,iterator=True)):
            chunk.to_sql(tblName, con=self.engine, index=False, if_exists='append')
            print('loop Num -->',inx)
        print('tbl created --> ', tblName)

    def tbl2Csv(self,pathout,query):

        df = self.getDataFrame(query)
        df.to_csv(pathout,header=True,index=False)

    @property
    def getConStringMysql(self):
        return """mysql+pymysql://{0}:{1}@{2}/{3}""".format(self.conf['user'],self.conf['password'],self.conf['host'],self.conf['database'])

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.dispose()


