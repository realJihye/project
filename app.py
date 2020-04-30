from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@13.209.50.238', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

# API
@app.route('/api/likes', methods=['POST'])
def write_review():
    print(request.form)
    category = request.form['category']
    like = db.categories.find_one({'name': category},{'_id':0})['like']
    db.categories.update_one({'name':category}, {'$set':{'like':like+1}})
    print(category + ' like ' + str(like+1))
    return jsonify({'result': 'success', 'msg': 'review success!', 'like': like+1})

@app.route('/api/likes', methods=['get'])
def get_like():
    category = request.args.get('category')
    print('like ' + category)
    like = db.categories.find_one({'name': category}, {'_id':0})['like']
    return jsonify({'result':'success', 'like': like})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)