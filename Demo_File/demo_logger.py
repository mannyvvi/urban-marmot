def logger():
    ##Start up
    import file_writer


    filename = 'testing_doc.csv' #sets target filename
    f = open(filename, 'w') #creates file to ensure no errors
    f.close() #closes file to allow it to be used elsewhere






    ##Write File
    lista = []
    file_writer.writer(lista,filename)

        
