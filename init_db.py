from pymongo import MongoClient
client = MongoClient('localhost', 27017) 
db = client.dbsparta

categories = ['Noodle', 'Bicycle', 'Museum', 'Hanok', 'Spa', 'Chicken', 'Local Market', 'Hiking',
            'Cafe', 'Hanriver', 'Hotteok', 'Chill', 'BBQ', 'Bibimbap', 'Octupus', 'Nightview']


for category in categories:
    db.categories.insert_one({'name': category, 'like': 0})