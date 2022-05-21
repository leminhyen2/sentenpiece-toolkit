
def writeListOfSPMvocabsToFile(spmModelFilePath, outputFileName):

    import sentencepiece as spm

    nameOfModelFile = spmModelFilePath
    spmModel = spm.SentencePieceProcessor(model_file= nameOfModelFile)

    listOfSPMvocabs = [spmModel.id_to_piece(id) for id in range(spmModel.get_piece_size())]

    def printListToTextFile(listToPrint, name):
        print(*listToPrint, sep='\n', file=open(name, "w", encoding="utf8"))
        return "print list to txt file"

    printListToTextFile(listOfSPMvocabs, outputFileName)


# Example: writeListOfSPMvocabsToFile('spm.en.nopretok.model', "englishVocab.txt")