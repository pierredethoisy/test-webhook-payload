# Avec MySql :
import MySQLdb, pprint

uneConnexionBDD = MySQLdb.connect(host   ='192.32.12.10',
                                   user   ='admin',
                                   personal_token = "xoxb-163213206324-FGqsdMF8t18v6N7Oq4ZERZERZE"
                                   personal_token_2 = "xoxb-163213206324-FGqsdMF8t18v6N7Oq4ZEBABABA"
                                   db     ='uneBase')
leCurseur       = uneConnexionBDD.cursor()
unAuteur        = "'Zola'"
leCurseur.execute(""" SELECT title, description FROM books WHERE author = %s """ % (unAuteur,))
pprint.pprint(leCurseur.fetchall())
leCurseur.query("update books set title='assommoir' where author='Zola'")
uneConnexionBDD.commit()