def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
 ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
 ##Boolean Parameters
 ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {'Signal_Loss':False, 'Shock_Alert':False,'Oxygen_Supply':False,'Fever':False,'Hypotension':False,'Hypertension':False}
    if(Singal_Loss == True):
        BasicResult['Signal Loss']=True
    if(Shock_Alert == True):
        BasicResult['Shock_Alert']=True 
    if(Oxygen_Supply == True):
        BasicResult['Oxygen_Supply']=True 
    if(Fever == True):
        BasicResult['Fever']=True
    if(Hypotension == True):
        BasicResult['Hypotension']=True
    if(Hypertension == True):
        BasicResult['Hypertension']=True 

    return BasicResult
