
class input_api:

    def __init__(self, user_id, age, gender, Heart_Rate, Systolic_BP, Diastolic_BP, Heart_O2_Level, Body_temp, time):

        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.Heart_Rate = Heart_Rate
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.Heart_O2_Level = Heart_O2_Level
        self.Body_temp = Body_temp
        self.time = time
        self.dic = {"Heart_Rate": Heart_Rate,
                    "Diastolic_BP": Diastolic_BP, "Systolic_BP":Systolic_BP, "Heart_O2_Level": Heart_O2_Level,
                    "Body_temp": Body_temp}

    def filter(data):
        wrong_flag = -1
        noise = 500
        if data > noise:
            data = wrong_flag
        return data



    def implement_filter(self):
        for key in self.dic.keys():
            if (key != "user_id" and key != "age" and key != "gender" and key != "time"):
                tmp = filter(self.dic[key])
                self.dic[key] = tmp



    def return_request(self, wire):
        alert = 1
        data_db = 2
        if (wire == alert):
            user_data_dic = {"Heart_Rate'": self.Heart_Rate,
                    "Diastolic_BP": self.Diastolic_BP, "Systolic_BP": self.Systolic_BP, "blood_oxygen": self.blood_oxygen, 
                    "Body_temp": self.temperature, "time": self.time}
            return user_data_dic
        if (wire == data_db):
            return self.user_id, self.dic
        
        
# my_data = input_api('Jack', 10, 'male', sensor.heart_rateSensor.get_heart_rate(), sensor.blood_pulse.get_blood_pulse(), sensor.blood_pulse.get_blood_pulse(), sensor.heart_o2Sensor.get_heart_o2(), sensor.body_tempSensor.get_body_temp(), sensor.time.get_time())
# print(my_data.dic)
# # my_data.implement_filter()
# # print(my_data.dic)
# my_data.return_request("alert")
