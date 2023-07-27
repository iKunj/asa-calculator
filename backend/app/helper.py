import json

'''
Global Values to use 
In future if API changes the type then just change here
and no need to change anywhere else
'''
RCSB_INTERFACE_PARTNER = "rcsb_interface_partner"
INTERFACE_PARTNER_IDENTIFIER = "interface_partner_identifier"
INTERFACE_PARTNER_FEATURE = "interface_partner_feature"
INTERFACE_PARTNER_FEATURE_POSITIONS = "feature_positions"
ASA_UNBOUND = "ASA_UNBOUND"
ASA_BOUND = "ASA_BOUND"
TABLE_DATA = "table_data"


# Added Features
IS_ROUND = False  # If rouding is needed for resulting substraction
ROUND_INT = 2  # Upto what decimal points

'''
Helper function for '/asa-change' endpoint
This uses the response received from the API and then parses the information
and generates the output as required
'''
def bodyParser(data):
    final_data = []
    # Looping through all the INTERFACE PARTNERS   
    for x in data[RCSB_INTERFACE_PARTNER]:
        
        # Extracting the header information i.e. entity_id & asym_id
        header = x[INTERFACE_PARTNER_IDENTIFIER]

        data = x[INTERFACE_PARTNER_FEATURE]
        unbound_data = []
        bound_data = []

        # Looping through all the FEATURE POSITIONS
        for y in data:
            # type_pos = len(y[INTERFACE_PARTNER_FEATURE_POSITIONS]) - 1
            # print("Type POS: ", type_pos)
            
            # Check for the type and based on the type loop through its FEATURE POSITIONS
            # and extend the array to include all of those
            if y["type"] == ASA_UNBOUND: 
                for z in y[INTERFACE_PARTNER_FEATURE_POSITIONS]:
                    unbound_data.extend(z["values"])
            elif y["type"] == ASA_BOUND:
                for z in y[INTERFACE_PARTNER_FEATURE_POSITIONS]:
                    bound_data.extend(z["values"])
                
        # print(len(bound_data), len(unbound_data))

        # This loop is necessary for react frontend wherein I am making a
        # array of object which is easily readable by react for table data purposes
        table_data = []
        for x in range(len(bound_data)):
            table_data.append({
                "srno" : x+1, 
                "unboundasa" : unbound_data[x], 
                "boundasa": bound_data[x], 
                "changeasa": round((unbound_data[x]-bound_data[x]), ROUND_INT) if IS_ROUND else unbound_data[x]-bound_data[x] # Here I have implemented single line round condition if its true then round else don't round
                })

        '''
        # BASIC PRINTING OF INFORMATION FOR DEBUG PURPOSES
        print("\nHEADER: ", header)
        print("\nTABLE DATA: ", table_data)
        print("\nDATA: ", data)
        print("\nUNBOUND: ", unbound_data)
        print("\nBOUND: ", bound_data)
        '''

        # Formatting the data as required 
        inter_data = {
            INTERFACE_PARTNER_FEATURE : header,
            TABLE_DATA : table_data
        }

        final_data.append(inter_data)
    return final_data

'''
This helper function is used to change the global
value of IS_ROUND & ROUND_INT.
This interacts with the React UI to give flexibility
in the change in ASA field to round values as needed
'''
def roundSwitcher(flag, value):
    global IS_ROUND, ROUND_INT
    try:
        IS_ROUND = flag
        ROUND_INT = value
        return True
    except:
        return False


'''
FOR TESTING PURPOSE ONLY
Can make use of a file so that we don't need to call the API again and again
f = open("data.json")
data = json.load(f)
# json_object = json.dumps(final_data)
# print("FINAL DATA: ", json_object)
# print(data)
# f.close()
'''