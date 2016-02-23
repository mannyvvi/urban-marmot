def logger():
    ##Start up
    import file_writer_4


    filename = 'testing_doc.txt' #sets target filename
    f = open(filename, 'w') #creates file to ensure no errors
    f.close() #closes file to allow it to be used elsewhere






    ##Write File
    lista = []
    file_writer_4.writer(lista,filename)

        
