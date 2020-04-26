from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@13.209.50.238', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

## API
# @app.route('/ps', methods=['POST'])
# def write_review():
#     title_receive = request.form['title_give']
#     author_receive = request.form['author_give']
#     review_receive = request.form['review_give']

#     db.reviews.insert_one({'title':title_receive, 'author':author_receive, 'review':review_receive })

#     return jsonify({'result': 'success', 'msg': 'review success!'})

# @app.route('/reviews', methods=['GET'])
# def read_reviews():
#     reviews = list(db.reviews.find({},{'_id':0}))
#     return jsonify({'result':'success', 'reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)