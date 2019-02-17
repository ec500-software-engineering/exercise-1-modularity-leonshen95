
import numpy as np
from Database_Module import DataBaseModule
# Input: ID(from main function perhaps), infoDB(from Database function)
# output: Three predicted parameters, three Alert signals(Type:Boolean


class AI_module(object):
    def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.Heart_Rate = Heart_Rate
        self.Heart_O2_Level = Heart_O2_Level
        self.Body_temp = Body_temp

    def Query_Data_From_Database(self,ID,infoDB):
        ## connect database, query previous one day data from Database
        # Database = database_dict()
        Heart_Rate=list()
        Blood_oxygen=list()
        Blood_pressure = list()
        Systolic= list()
        Diastolic= list()
        DataBaseModule.search(ID)
        # Username = input("")
        #get dictionary from database
        for key in infoDB:
            if key== ID:
                # pressure = dict.get('blood_pressure')
                Heart_Rate=dict.get('Heart_Rate')
                oxygen = dict.get('blood_oxygen')
                Diastolic_BP = dict.get('Diastolic_BP')
                Systolic_BP = dict.get('Systolic_BP')
                # Blood_pressure.append(pressure)
                Heart_Rate.append(Heart_Rate)
                Blood_oxygen.append(oxygen)
                Systolic.append(Systolic_BP)
                Diastolic.append(Diastolic_BP)

        return Heart_Rate, Blood_oxygen, Systolic,Diastolic

    def AI_Module(self,Heart_Rate,Systolic,Diastolic,Blood_oxygen, Body_temp):

        ## AI module do the prediction, The AI module uses previous data
        rate = np.array(Heart_Rate)
        oxygen=np.array(Blood_oxygen)
        # pressure = np.array(Blood_pressure)
        diastolic = np.array(Diastolic)
        systolic = np.array(Systolic)
        temp = np.array(Body_temp)
        # pressure_predict_result = np.mean(pressure)
        rate_predict_result = np.mean(rate)
        oxygen_predict_result = np.mean(oxygen)
        Diastolic_predict_result = np.mean(diastolic)
        Systolic_predict_result = np.mean(systolic)
        Temp_predict_result = np.mean(temp)


        return rate_predict_result, oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result,Temp_predict_result

    def Feedback(self,rate_predict_result, Blood_oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result,Temp_predict_result):
        lower_BP= 80
        upper_BP= 120
        lower_rate = 55
        upper_rate = 100
        lower_BO = 80
        upper_BO = 120
        BP_Alert= False
        BO_Alert = False
        Temp_Alert = False

        Pulse_Alert =False
        if(Blood_oxygen_predict_result<lower_BO or Blood_oxygen_predict_result>upper_BO):
            BO_Alert =True
        if(rate_predict_result<lower_rate or rate_predict_result>upper_rate):
            BP_Alert =True
        if(Systolic_predict_result< lower_BP or Diastolic_predict_result <lower_BP or Systolic_predict_result > upper_BP or Diastolic_predict_result > upper_BP):
            Pulse_Alert =True
        if(Temp_predict_result<35 or Temp_predict_result>38):
            Temp_Alert =True
        ## feedback the AI prediction result to the interface
        ## It will turn on the Alert when the statues get worse.
        return BO_Alert,BP_Alert,Pulse_Alert,Temp_Alert


