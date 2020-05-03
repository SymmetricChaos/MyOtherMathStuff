
# Differences between prediction funcion f(x) and data y
# Optionally raised to a power, usually squared
def residuals(X,Y,f,p=1):    
    return [abs(y-f(x))**p for x,y in zip(X,Y)]  


# Differences between some central point c and actual values
# Optionally raised to a power, usually squared
def errors(D,c,p=1):
    return [abs(d-c)**p for d in D]





if __name__ == '__main__':
    
    import numpy as np
    
    x = np.linspace(0,10,100)
    y = x+np.random.standard_normal(100)
    
    def model(x):
        return x
    
    median_abs_dev = np.median(residuals(x,y,model))
    mean_sq_dev = np.mean(residuals(x,y,model,p=2))
    
    print("Data with Standard Normal Error Term")
    print(f"Median Absolute Deviations: {median_abs_dev:.3}")
    print(f"Mean Squared Deviations:    {mean_sq_dev:.3}")