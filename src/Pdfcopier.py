
import os
import src.PlotexSettings as Settings

class Pdfcopier:
    def __init__(self,args):
       
        outputPath = Settings.plotexPath + '/' + Settings.output + '/' + Settings.tmpfile + '.pdf'
        localPath = Settings.localPath

        localfile = args.filename.split('.')
        if len(localfile)>1:
            localfile = localfile[:-1]
    
        localfile = ''.join(localfile)

        filename = localPath + '/' + localfile + '.pdf'

        copyCMD = 'cp {outfile} {localfile}'
        copyCMD = copyCMD.format(outfile=outputPath,localfile=filename)
        os.system(copyCMD)
