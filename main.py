import input_api
import Analyzer
import Database_Module

import AI_module
import OutputAlert_module

class main:

    ## Input_api Module
    ## When I tried to implement filter to get the keys(user ID, gender and age), there is an error saying: 
    ## "  tmp = filter(self.dic[key]) TypeError: filter expected 2 arguments, got 1" 
    ## Except getting errors while filtering keys(user ID, gender and age), others work fine.
    
    my_data = input_api.input_api('a', 1, 'male', 1, 1, 10000, 1, 1, 1) #sample input
    # my_data = input_api.input_api(input("Simulated input here"))
    my_data.implement_filter()
    print(my_data.dic)
    my_data.return_request("alert")
    Keys = my_data.implement_filter()
    print(Keys.dic)

    ## Analyser Module
    Analysed_data = Analyzer.Analyzer(**my_data.dic)
    print(Analysed_data.__dict__)
    Analysed_signal_Loss = Analyzer.Analyzer.Signal_Loss(Analysed_data,Heart_Rate=Analysed_data.Heart_Rate,Body_temp=Analysed_data.Body_temp)
    Analysed_shock_alert = Analyzer.Analyzer.Shock_Alert(Analysed_data,Heart_Rate=Analysed_data.Heart_Rate,Body_temp=Analysed_data.Body_temp)
    Analysed_fever = Analyzer.Analyzer.Fever(Analysed_data,Body_temp=Analysed_data.Body_temp)
    Analysed_hypertension = Analyzer.Analyzer.Hypertension(Analysed_data,Systolic_BP=Analysed_data.Systolic_BP,Diastolic_BP=Analysed_data.Diastolic_BP)
    Analysed_oxygen_supply = Analyzer.Analyzer.Oxygen_Supply(Analysed_data,Heart_O2_Level=Analysed_data.Heart_O2_Level)
    Analysed_hypotension = Analyzer.Analyzer.Hypotension(Analysed_data,Systolic_BP=Analysed_data.Systolic_BP,Diastolic_BP=Analysed_data.Diastolic_BP)

    
    ## Database Module
    ## Because the keys(user ID, gender and age) of input are getting errors in input_api module, database cannot store data without valid ID.
  
    Database_Module.DataBaseModule.authen(Analysed_data)
    Database_Module.DataBaseModule.insert(Analysed_data,ID=,info=)
    Database_Module.DataBaseModule.delete(Analysed_data,ID=)
    Database_Module.DataBaseModule.search(Analysed_data,ID=)

    
    ## AI Module
    ## There is some mismatch in variable. "Blood_pressure" is a new variable occurred in AI module that we cannot find identical variable from previous modules.
    
    prediction = AI_module.AI_module(**my_data.dic)
    print(**prediction.__dict__)
    AI_module.AI_module.Query_Data_From_Database(prediction,ID=,infoDB=)
    AI_module.AI_module.AI_Module(prediction,Blood_oxygen=Analysed_data.Heart_O2_Level,Blood_pressure=Analysed_data.,Systolic=Analysed_data.Systolic_BP,Diastolic=Analysed_data.Diastolic_BP)
    AI_module.AI_module.Feedback(prediction,Blood_pressure_predict_result=prediction.AI_Module().,Blood_oxygen_predict_result=prediction.AI_Module().Blood_oxygen,Diastolic_predict_result=prediction.AI_Module().Diastolic,Systolic_predict_result=prediction.AI_Module().Systolic)

    
    ## Display Module
    OutputAlert_module.receive_basic_iuput_data(Singal_Loss=Analysed_signal_Loss,Shock_Alert=Analysed_shock_alert,Oxygen_Supply=Analysed_oxygen_supply,Fever=Analysed_fever,Hypotension=Analysed_hypotension,Hypertension=Analysed_hypertension)
    OutputAlert_module.display_AI_iuput_data()