from flask import Flask, render_template, request, redirect 
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    checkout = request.form
    count = 0
    now = datetime.now()
    time = now.strftime("%B %d %Y, %I:%M:%S %p")
    for fruit in checkout:
        if (fruit == "last_name" or fruit == "student_id"):
            pass
        elif(fruit == "first_name"):
            name = checkout[fruit]
        else:
            count+=int(checkout[fruit])
    print(f"Charging {name} for {count} fruits.")
    return render_template("checkout.html",checkout=checkout,count = count, time=time )
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    