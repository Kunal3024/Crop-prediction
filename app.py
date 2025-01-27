import pickle
from flask import redirect, Flask, render_template, request, url_for

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def hello_world():
    ans = None
    if request.method == 'POST':
        n=request.form.get("n")        
        p=request.form.get("p")
        k=request.form.get("k")
        t=request.form.get("t")
        h=request.form.get("h")
        ph=request.form.get("ph")
        rf=request.form.get("rf")
        
        def pred(n,p,k,t,h,ph,rf):
            model=pickle.load(open('rf.pkl','rb'))
            return model.predict([[n,p,k,t,h,ph,rf]])[0]
        
        ans = pred(n,p,k,t,h,ph,rf)
        return redirect(url_for('res', ans=str(ans)))
    
    return render_template('index.html', ans = ans)

@app.route('/result', methods=['GET','POST'])
def res():
    ans = request.args.get('ans', default="Try again", type = str)
    return render_template('results.html', ans = ans)

if __name__ == '__main__':
    app.run(debug=True)
