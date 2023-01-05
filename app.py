from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
#post request happens when the client requests data from the server, that it then provides
#get request is where the server returns the data [displaying information on a webpage]
def predict():
    if request.method == 'POST':
        #retrieve data from fields
        p1 = int(request.form['p1'])
        p2 = request.form['p2']
        if (p2 == "Yes"):
            p2 = 1
        else:
            p2 = 0
        p3 = request.form['p3']
        if p3 == "Yes":
            p3 = 1
        else:
            p3 = 0

        p4 = int(request.form['p4'])
        p5 = float(request.form['p5'])
        p6 = int(request.form['p6'])
        p7 = float(request.form['p7'])
        p8 = float(request.form['p8'])
        p9 = int(request.form['p9'])
        p10 = float(request.form['p10'])
        p11 = float(request.form['p11'])
        p12 = int(request.form['p12'])
        p13 = float(request.form['p13'])
        p14 = float(request.form['p14'])
        p15 = int(request.form['p15'])
        p16 = float(request.form['p16'])
        p17 = int(request.form['p17'])
      

        input = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17]

        probs = model.predict_proba([input])

        prob0 = probs[0][0] * 100
        prob1 = probs[0][1] * 100

        prediction = "There is a " + str(prob0) + " percent probability that this customer will stay with current telecommunications provider."
        prediction2 = "There is a " + str(prob1) + " percent probabiltiy that this customer will change telecommunications providers."

        overall = prediction + prediction2;
        return render_template('index.html',prediction_texts=overall)


    else:
        return render_template('index.html')






if __name__ == "__main__":
    app.run(port = 3000, debug = True)

