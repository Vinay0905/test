from flask import Flask,request,render_template



app=Flask(__name__)

@app.route('/')
def welcome():
    return "###welcome to the flask###" 

@app.route('/calculate',method=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    else:
    
        result=number1-number2

print(__name__)

if __name__== '__main__':
    app.run(debug=True)







