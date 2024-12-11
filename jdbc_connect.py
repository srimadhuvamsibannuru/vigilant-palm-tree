from sqlalchemy import create_engine
jdbcurl = ''
jdbbdatabasename = ''
jdbcusername = ''
jdbcpwd = ''
jdbcportnumber = ''


engine_url = "mysql://"+jdbcusername+":"+jdbcpwd+"@"+jdbcurl+":"+jdbcportnumber+"/"+jdbbdatabasename
engine = create_engine(engine_url)

connection = engine.connect()

data = connection.execute("select * from dbo.test")
