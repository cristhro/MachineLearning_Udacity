def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    from sklearn.naive_bayes import GaussianNB
    # Creamos el clasificador
    clf = GaussianNB()
    
    clf.fit(features_train, labels_train)  #Le pasamos como parametros las  (features, labels)
    
    return clf
    