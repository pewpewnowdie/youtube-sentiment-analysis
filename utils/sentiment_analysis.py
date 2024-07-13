import time
from keras.preprocessing.sequence import pad_sequences
import keras
import pickle
import re
import string

with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = keras.models.load_model('model.h5')

def decode_sentiment(score, include_neutral=True):
    if include_neutral:        
        label = 'NEUTRAL'
        if score <= 0.4:
            label = 'NEGATIVE'
        elif score >= 0.7:
            label = 'POSITIVE'

        return label
    else:
        return 'NEGATIVE' if score < 0.5 else 'POSITIVE'

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def predict(text, include_neutral=True):
    start_at = time.time()
    text = preprocess_text(text)
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=300)
    score = model.predict([x_test])[0]
    label = decode_sentiment(score, include_neutral=include_neutral)

    return {"label": label, "score": float(score),
       "elapsed_time": time.time()-start_at}  