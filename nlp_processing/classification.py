from transformers import pipeline

def classify_disaster(text):
    classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')
    labels = ['flood', 'earthquake', 'wildfire', 'hurricane', 'pandemic', 'tornado', 'volcano eruption', 'drought']
    result = classifier(text, candidate_labels=labels)
    return result