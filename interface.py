from flask import Flask,render_template,jsonify,request
from Project.utils import BankChurn
import config

app = Flask(__name__)

@app.route("/")
def test():
    return "successfull"

@app.route("/pred",methods = ["GET"])
def bank():
    data = request.form

    CreditScore     = eval(data["CreditScore"])
    Gender          = data["Gender"]
    Age             = eval(data["Age"])
    Tenure          = eval(data["Tenure"])
    Balance         = eval(data["Balance"])
    NumOfProducts   = eval(data["NumOfProducts"])
    HasCrCard       = eval(data["HasCrCard"])
    IsActiveMember  = eval(data["IsActiveMember"])
    EstimatedSalary = eval(data["EstimatedSalary"])
    Geography       = "Geography__"+data["Geography"]

    obj = BankChurn(CreditScore,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography)
    prd = obj.get_prediction()

    dict1 = {0:"Leave",1:"Not leave"}
    return jsonify({"result":f"The customer will {dict1[prd[0]]}"})

if __name__ == "__main__":
    app.run(port = config.port_number)

