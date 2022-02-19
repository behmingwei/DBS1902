#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBSReg_MT")
        pred = model.predict([[float(rates)]])
        s = "Predicted DBS share price based on linear regression model: " + str(pred)
        
        model = joblib.load("DBSDT_MT")
        pred = model.predict([[float(rates)]])
        s2 = "Predicted DBS share price based on linear regression model: " + str(pred) 
        
        model = joblib.load("DBSNN_MT")
        pred = model.predict([[float(rates)]])
        s3 = "Predicted DBS share price based on linear regression model: " + str(pred)
        
        return(render_template("index.html", result1 = s, result2 = s2, result3 = s3))
    else:
        return(render_template("index.html", result1 = "2", result2 = "2", result3 = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




