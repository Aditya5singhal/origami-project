from tracemalloc import take_snapshot
from flask import Flask,jsonify,request
app=Flask(__name__)

tasks=[
    {
        'id':1,
        'title':'list of utensils',
        'description':'whitehat jr',
        'done':False
        
    },
      {
        'id':2,
        'title':'list of cloths',
        'description':'whitehat jr is great for coding',
        'done':False
        
    },
    
]
@app.route('/')



def hello():
    return 'hi'
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide correct data'
            
        },400)
        
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
        
    }
    tasks.append(task)
    return jsonify({
        'status':'success',
            'message':'successful' 
    })
    
    @app.route('/get-data')
    def get_task():
        return jsonify({'data':tasks})

if(__name__=='__main__'):
    app.run(debug=True)