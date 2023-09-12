def linearPhenotypeRegression(csv_file,
                              var1=None,
                              var2=None):
    # fitting a linear regression on the height and the 
    # bolting time of the lettuce phenotypes to see the
    # linear regression of the height and the bolting time
    import pandas as pd
    from scipy import stats
    import pickle as pic
    if var1 and var2 != "None":
        csv_file = csv_file
        read_phenotype = pd.read_csv(csv_file, sep = ",").dropna()
        X = read_phenotype[var1].apply(lambda n: int(n))
        y = read_phenotype[var2].apply(lambda n: int(n))
        slope, intercept, r, p, str_err = stats.linregress(X,y)
        prediction_model = list(map(lambda n: slope * X + intercept,X))
        return tuple([slope, r, p])
