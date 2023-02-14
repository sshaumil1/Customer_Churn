import numpy as np
import config
import json
import pickle

class BankChurn():
    def __init__(self,CreditScore,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography):
        self.CreditScore     = CreditScore
        self.Gender          = Gender
        self.Age             = Age
        self.Tenure          = Tenure
        self.Balance         = Balance
        self.NumOfProducts   = NumOfProducts
        self.HasCrCard       = HasCrCard
        self.IsActiveMember  = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Geography       = Geography

    def models(self):
        with open (config.model_path,"rb") as f:
            self.model = pickle.load(f)
        
        with open (config.scaling_path,"rb") as f:
            self.scaling = pickle.load(f)

        with open (config.column_path,"r") as f:
            self.column = json.load(f)

    def get_prediction(self):
        self.models()
        test_array    = np.zeros(len(self.column["columns"]))

        test_array[0] = self.CreditScore
        test_array[1] = self.column["Gender"][self.Gender]
        test_array[2] = self.Age
        test_array[3] = self.Tenure
        test_array[4] = self.Balance 
        test_array[5] = self.NumOfProducts
        test_array[6] = self.HasCrCard
        test_array[7] = self.IsActiveMember
        test_array[8] = self.EstimatedSalary
        a = np.where(self.column["columns"] == self.Geography)[0]
        test_array[a] = 1

        scal  = self.scaling.transform([test_array])
        churn = self.model.predict(scal)

        return churn
       




