from django.db import connection
#----------------------------------------------------------------------

sql ="""
SELECT * FROM T_TASKINFO
WHERE ENTERPRISEINVOLED=1 
AND DISCOVERTIME BETWEEN TO_DATE ( '%(start_time)s', 'yyyy-MM-dd HH24:mi:ss' ) 
		AND TO_DATE ( '%(end_time)s', 'yyyy-MM-dd HH24:mi:ss' ) 
		
"""


def on_and_off_task(start,end):
    """"""
    
    dc ={
        'start_time':start,
        'end_time':end
    }
    cursor = connection.cursor()
    cursor.execute(sql%dc )
    a1=[]
    for row in cursor:
        row_dc ={}
        for col_data, col in zip(row, cursor.description):
            row_dc[col[0]]=col_data
        a1.append(row_dc)  
    return a1