import input_api
import Analyzer

import AI_module
import OutputAlert_module

import sensor

class main:
    # def print_time(input,delay):
    #     count = 0
    #     while count < 5:
    #         time.sleep(delay)
    #         count += 1
    #         print"%s: %s:"%(input,time.ctime(time.time()))
    # try: _thread.start_new_thread(print_time,"Thread" + count)
    # except:
    #     print("Error")
    # while True:
    #     pass
    ## Input_api Module
    ## When I tried to implement filter to get the keys(user ID, gender and age), there is an error saying:
    ## "  tmp = filter(self.dic[key]) TypeError: filter expected 2 arguments, got 1"
    ## Except getting errors while filtering keys(user ID, gender and age), others work fine.

    my_data = input_api.input_api('Jack', 10, 'male', sensor.heart_rateSensor.get_heart_rate(),
                                  sensor.blood_pulse.get_blood_pulse(), sensor.blood_pulse.get_blood_pulse(),
                                  sensor.heart_o2Sensor.get_heart_o2(), sensor.body_tempSensor.get_body_temp(),
                                  sensor.time.get_time()) #sample input
    # my_data = input_api.input_api(input("Simulated input here"))
    # my_data.implement_filter()
    print(my_data.dic)
    my_data.return_request("alert")
    # Keys = my_data.implement_filter()
    # print(Keys.dic)

    ## Analyser Module
    Analysed_data = Analyzer.Analyzer(**my_data.dic)
    print("Analysing stage...")
    print(Analysed_data.__dict__)
    Analysed_signal_Loss = Analyzer.Analyzer.Signal_Loss(Analysed_data, Heart_Rate=Analysed_data.Heart_Rate,
                                                         Body_temp=Analysed_data.Body_temp)
    Analysed_shock_alert = Analyzer.Analyzer.Shock_Alert(Analysed_data, Heart_Rate=Analysed_data.Heart_Rate,
                                                         Body_temp=Analysed_data.Body_temp)
    Analysed_fever = Analyzer.Analyzer.Fever(Analysed_data, Body_temp=Analysed_data.Body_temp)
    Analysed_hypertension = Analyzer.Analyzer.Hypertension(Analysed_data, Systolic_BP=Analysed_data.Systolic_BP,
                                                           Diastolic_BP=Analysed_data.Diastolic_BP)
    Analysed_oxygen_supply = Analyzer.Analyzer.Oxygen_Supply(Analysed_data, Heart_O2_Level=Analysed_data.Heart_O2_Level)
    Analysed_hypotension = Analyzer.Analyzer.Hypotension(Analysed_data, Systolic_BP=Analysed_data.Systolic_BP,
                                                         Diastolic_BP=Analysed_data.Diastolic_BP)

    ## Database Module
    ## Because the keys(user ID, gender and age) of input are getting errors in input_api module, database cannot store data without valid ID.

    # Database_Module.DataBaseModule.authen(Analysed_data)
    # Database_Module.DataBaseModule.insert(Analysed_data, ID=, info=)
    # Database_Module.DataBaseModule.delete(Analysed_data, ID=)
    # Database_Module.DataBaseModule.search(Analysed_data, ID=)

    ## AI Module
    ## There is some mismatch in variable. "Blood_pressure" is a new variable occurred in AI module that we cannot find identical variable from previous modules.

    prediction = AI_module.AI_module(**my_data.dic)
    print('Predicting stage...:')
    print(prediction.__dict__)
    # AI_module.AI_module.Query_Data_From_Database(prediction, ID=, infoDB=)
    AI_module.AI_module.AI_Module(prediction, Heart_Rate=prediction.Heart_Rate, Systolic=prediction.Systolic_BP,
                                  Diastolic=prediction.Diastolic_BP,Blood_oxygen=prediction.Heart_O2_Level,Body_temp=prediction.Body_temp)
    # AI_module.AI_module.Feedback(prediction, rate_predict_result=prediction.Heart_Rate,
    #                              Blood_oxygen_predict_result=prediction.Heart_O2_Level,
    #                              Diastolic_predict_result=prediction.AI_Module().Diastolic_predict_result,
    #                              Systolic_predict_result=prediction.AI_Module().Systolic_predict_result)
    def Feedback(self, rate_predict_result, Blood_oxygen_predict_result, Diastolic_predict_result,
                 Systolic_predict_result, Temp_predict_result):
        lower_BP = 80
        upper_BP = 120
        lower_rate = 55
        upper_rate = 100
        lower_BO = 80
        upper_BO = 120
        BP_Alert = False
        BO_Alert = False
        Temp_Alert = False

        Pulse_Alert = False
        if (Blood_oxygen_predict_result < lower_BO or Blood_oxygen_predict_result > upper_BO):
            BO_Alert = True
        if (rate_predict_result < lower_rate or rate_predict_result > upper_rate):
            BP_Alert = True
        if (
                Systolic_predict_result < lower_BP or Diastolic_predict_result < lower_BP or Systolic_predict_result > upper_BP or Diastolic_predict_result > upper_BP):
            Pulse_Alert = True
        if (Temp_predict_result < 35 or Temp_predict_result > 38):
            Temp_Alert = True
        ## feedback the AI prediction result to the interface
        ## It will turn on the Alert when the statues get worse.
        return BO_Alert, BP_Alert, Pulse_Alert, Temp_Alert

    ## Display Module
    Alert = OutputAlert_module.receive_basic_iuput_data(Singal_Loss=Analysed_signal_Loss, Shock_Alert=Analysed_shock_alert,
                                                Oxygen_Supply=Analysed_oxygen_supply, Fever=Analysed_fever,
                                                Hypotension=Analysed_hypotension, Hypertension=Analysed_hypertension)


    rate, oxygen, diastolic, systolic, temp = AI_module.AI_module.AI_Module(prediction,Analysed_data.Heart_Rate,Analysed_data.Systolic_BP,Analysed_data.Diastolic_BP,Analysed_data.Heart_O2_Level,Analysed_data.Body_temp)
    print('Heart rate prediction:')
    print(rate)
    print('blood oxygen prediction:')
    print(oxygen)
    print('Systolic blood pressure prediction:')
    print(systolic)
    print('Diastolic blood pressure prediction:')
    print(diastolic)
    print('Temperature prediction:')
    print(temp)
    print(Alert)
