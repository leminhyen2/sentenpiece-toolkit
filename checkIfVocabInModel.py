
def checkIfVocabInModel(vocabToCheck, modelFilePath):
    import sentencepiece.sentencepiece_model_pb2 as model

    m = model.ModelProto()
    m.ParseFromString(open(modelFilePath, "rb").read())

    for i, vocab in enumerate(m.pieces):
        vocabContent = vocab.piece
        if (vocabContent == vocabToCheck):
            return True
    
    return False

# print(checkIfVocabInModel("🐬", "new.model"))