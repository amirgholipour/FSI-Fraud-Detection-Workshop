import os
import zipfile
def get_hyper_paras():
    BATCH = 64
    EPOCHS = 100
    model_Type = 'ml'
    model_Name = 'LogisticRegression'
    
    # dataPath = "../data/raw/creditcard.csv"
    with zipfile.ZipFile('../data/raw/creditcard.csv.zip', 'r') as zip_ref:
        zip_ref.extractall('../data/raw/')
    
    base, sourceRepoName = os.path.split(os.getcwd())
    base, sourceRepoName = os.path.split(base)
    refRepoName = sourceRepoName.replace('Workshop','Inference')
    # refRepoName = 'FSI-Fraud-Detection-Inference'
    if model_Type == 'ml':
    
        model_dir= base +'/'+refRepoName +'/'+ 'models/finalized_ml_model.pkl'
        # model_dir_workshop= base +'/'+sourceRepoName +'/'+ 'models/finalized_ml_model.pkl'
    else:
        model_dir= base +'/'+refRepoName +'/'+ 'models/finalized_dl_model.h5'
        # model_dir_workshop= base +'/'+sourceRepoName +'/'+ 'models/finalized_dl_model.h5'
        
    dataPath = base +'/'+sourceRepoName +'/'+'data/raw/creditcard.csv'
    refRepoDir = base +'/'+refRepoName 
    sourceRepoDir = base +'/'+sourceRepoName
    return dataPath,BATCH,EPOCHS,model_Type,model_Name, model_dir,refRepoName,sourceRepoName,refRepoDir,sourceRepoDir

