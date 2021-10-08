from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        'id':1,
        'no':123456789,
        'name':'Altair',
        'called':False
    },
    {
        'id':2,
        'no':234567890,
        'name':'Ezio',
        'called':False
    }
]

@app.route("/add-contact",methods=["Post"])
def AddContact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the details'
        })
    
    contact = {
        'id': contacts[-1]['id']+1,
        'no':request.json['no'],
        'name':request.json.get('name',""),
        'called':False
    }
    contacts.append(contact)

    return jsonify({
        'status':'success',
        'message':'no added'
    })

@app.route("/get-contacts")
def GetContacts():
    return jsonify({
        'data':contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)