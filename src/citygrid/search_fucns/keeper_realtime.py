from django.db import connection
#----------------------------------------------------------------------

sql ="""
SELECT * FROM T_INFO_MAIN
WHERE ( DISCOVERTIME BETWEEN TO_DATE ( '%(day)s 00:00:00', 'yyyy-MM-dd HH24:mi:ss' ) 
		AND TO_DATE ( '%(day)s 23:59:59', 'yyyy-MM-dd HH24:mi:ss' ) 
		AND KEEPERSN = '%(code)s'
		)
		
"""


def keeper_case_count(day,code):
    """
    """
    
    dc ={
        'day':day,
        'code':code
    }
    cursor = connection.cursor()
    cursor.execute(sql%dc )
    rows=[]
    for row in cursor:
        dc = {}
        for index, desp_item in enumerate(cursor.description):
            head_name = desp_item[0]
            dc[head_name] = row[index]
        rows.append(dc)    
    return rows