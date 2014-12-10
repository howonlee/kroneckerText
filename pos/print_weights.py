from tagger import PerceptronTagger

if __name__ == "__main__":
    tagger= PerceptronTagger(load="kron_deg")
    for key, val in tagger.model.weights.items():
        if u"degree" in key and len(val) < 10:
            print key, val
