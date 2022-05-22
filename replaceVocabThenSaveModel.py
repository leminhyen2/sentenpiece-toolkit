def replaceVocabThenSaveModel(updatedModelFileName, originalVocab, newVocab, score=0):
    import sentencepiece.sentencepiece_model_pb2 as model

    m = model.ModelProto()
    m.ParseFromString(open("spm.ja.nopretok.model", "rb").read())

    for i, vocab in enumerate(m.pieces):
        vocabContent = vocab.piece
        if (vocabContent == originalVocab):
            vocab.score = score
            vocab.piece = newVocab

    with open(updatedModelFileName, 'wb') as f:
        f.write(m.SerializeToString())


# replaceVocabThenSaveModel("new.model", "🐬", "<MASK>", 0)

# from writeListOfSPMvocabsToFile import writeListOfSPMvocabsToFile
# writeListOfSPMvocabsToFile("new.model", "englishVocab.txt")
