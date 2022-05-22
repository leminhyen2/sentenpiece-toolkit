
def writeListOfSPMvocabsToFile(spmModelFilePath, outputFileName="SPMvocabs.txt"):

    import sentencepiece.sentencepiece_model_pb2 as model

    m = model.ModelProto()
    m.ParseFromString(open(spmModelFilePath, "rb").read())

    listOfVocabs = []
    for i, vocab in enumerate(m.pieces):
        vocabContent = vocab.piece
        vocabScore = vocab.score
        listOfVocabs.append(f"{vocabContent}    {vocabScore}")

    def printListToTextFile(listToPrint, name):
        print(*listToPrint, sep='\n', file=open(name, "w", encoding="utf8"))
        return "print list to txt file"

    printListToTextFile(listOfVocabs, outputFileName)


# writeListOfSPMvocabsToFile('spm.ja.nopretok.model', "englishVocab.txt")