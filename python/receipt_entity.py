from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Rcpt_ent:
    def __init__(self):
        pass
    def insert(id, title, val, time):        
        try:
            int(val)
        except:
            return
        inst = "insert into Rcpt_ent (rcpt_id, title, value, time) values ('" + id +"', '" + title + "', " + val + ", '" + time + "')"
        db.engine.execute(text(inst))
    def update(id, title, val, time):
        try:
            int(val)
        except:
            return
        inst = "update Rcpt_ent set title='" + title + "', value=" + val + ", time='" + time + "' where id=" + id
        db.engine.execute(text(inst))
    def delete(id):
        inst = "delete from Rcpt_ent where id=" + id
        db.engine.execute(text(inst))
    def all():
        return db.engine.execute(""" 
            select id, rcpt_id parent_id, title, value, time from Rcpt_ent order by time desc;
        """).all()
    def sum():
        return db.engine.execute(""" 
            select ifnull(sum(value), 0) val from Rcpt_ent 
        """).first()['val']
    def max_mth():
        return db.engine.execute(""" 
            select ifnull(max(val), 0) val from (
                select year(time) year, month(time) month, sum(value) val from Rcpt_ent group by year(time), month(time)
            ) as t;
        """).first()['val']
    def max_yr():
        return db.engine.execute(""" 
            select ifnull(max(val), 0) val from (
                select year(time), sum(value) as val from Rcpt_ent group by year(time)
            ) as t;
        """).first()['val']
    def sum_mth():
        return db.engine.execute(""" 
            select year(time) year, month(time) month, sum(value) as val from Rcpt_ent group by year(time), month(time) order by year(time) ASC, month(time) ASC;
        """).all()

        