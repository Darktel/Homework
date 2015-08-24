# This file update object class 'Person' in date base

import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print (key, '\t=>', db[key])

sue = db['Sue jonse']
sue.giveRaise(.1)
db['Sue jonse'] = sue

db.close()
