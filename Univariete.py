class Univariete():

    def quanqual(dataset):
        quan=[]
        qual=[]
        for column_name in dataset.columns:
            #print(column_name)
            if(dataset[column_name].dtypes=='O'):
                #print("qual")
                qual.append(column_name)
            else:
                #print("quan")
                quan.append(column_name)
        return quan,qual