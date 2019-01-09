import os.path
import numpy as np

def create_output(path, curves):
    #print curves
    ph_range = np.arange(0,20.1,0.1)
    #file_name_template = "{}_{}_{}.csv"
    
    ph_values = np.empty((0, len(ph_range)))
    res_numbers = ["pH"]
    for key, curve in curves.items():
        #file_name = file_name_template.format(*key)
        #file_path = os.path.join(path, file_name)
        ph_values = np.append(ph_values, np.array([[x[1] for x in curve]]), axis = 0)
        res_numbers.append("_".join(key))
        """with open(file_path, "w") as f:
            for pH, value in curve:
                f.write(str(pH)+', '+str(value)+'\n')"""
    ph_values = np.vstack((ph_range, ph_values)).T
    with open(os.path.join(path, "AllTitrCurves.csv"), "w+") as outData:
        outData.write(",".join(res_numbers) + "\n" )
        for x in ph_values:
            outData.write(','.join(map(str, x)) + "\n")