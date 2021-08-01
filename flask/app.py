from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine
from api_constant import database_password


app = Flask(__name__)
# db = MongoEngine()  # default function is for localhost Mongo Engin.
db = MongoEngine()

database_name = "API"
db_url = "mongodb+srv://AK_310721:{}@cluster0.ujmxj.mongodb.net/{}?retryWrites=true&w=majority".format(
                    database_password, database_name)
app.config['MONGODB_HOST'] = db_url
db.init_app(app)


'''
simple request body
{
    'book_id':1,
    'name': "The sunshine",
    'auther':"Sagar Kadam"
}

'''

class Books(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    auther = db.StringField()

    def to_json(self):
        # convert json respance
        return {
            "book_id": self.book_id,
            "name": self.name,
            "auther": self.auther
        }

@app.route('/api/db_populate',  methods=['POST'])
def db_populate():
    book1 = Books(book_id=1, name="Secret", auther="Ram K")
    book2 = Books(book_id=2, name="Harry Porter", auther="Harry P")
    book1.save()
    book2.save()
    return make_response("", 201)

@app.route('/api/books', methods=['GET','POST'])
def api_books():
    print("print(request.method)", request.method)
    if request.method == "GET":
        print(request.method)
        books = []
        for book in Books.objects:
            books.append(book)
        return make_response(jsonify(books), 200)
    elif request.method == 'POST':
        '''
        simple request body
        {
            'book_id':1,
            'name': "The sunshine",
            'auther':"Sagar Kadam"
        }

        '''
        print(request.method)
        content = request.json
        book = Books(book_id = content['book_id'],
                         name = content['name'],
                         auther = content['auther'])
        book.save()
        return make_response("", 201)


# echo {"book_id":66, "name": "Master mind","auther":"Shake sphear"} | http POST http://127.0.0.1:5000/api/books
# http POST http://127.0.0.1:5000/api/books


@app.route('/api/books/<book_id>', methods=['GET','PUT','DELETE'])
def api_each_book(book_id):
    if request.method == 'GET':
        book = Books.objects(book_id = book_id).first()
        if book:
            return make_response(jsonify(book.to_json()), 200)
        else:
            return make_response('', 404)
    elif request.method == 'PUT':
        '''
        simple request body
        {
            'book_id':1,
            'name': "The sunshine",
            'auther':"Sagar Kadam"
        }

        '''
        content = request.json
        book_obj = Books.objects(book_id = book_id).first()
        book_obj.update(auther = content['auther'], name=content['name'])
        return make_response("",204)
    elif request.method == 'DELETE':
        book = Books.objects(book_id = book_id).first()
        book.delete()
        return make_response(" ", 206)
# http GET http://127.0.0.1:5000/api/books/6
# echo {"book_id":6, "name": "11 Master mind","auther":"11 Shake sphear"} | http PUT http://127.0.0.1:5000/api/books/6
# http DELETE http://127.0.0.1:5000/api/books/6

if __name__ == '__main__':
    app.run(debug=True)    #debug=True, host='0.0.0.0',port='5001')
