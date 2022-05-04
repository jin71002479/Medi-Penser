import json
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from django.http import JsonResponse
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder


def index(request):
    context={}
    return render(request, 'main/index.html',context)

def about(request):
    return render(request, 'main/about.html')

with open('model/intents.json','r', encoding="UTF-8") as file:
    data = json.load(file)
training_sentences = []
training_labels = []
labels = []
responses = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
        responses.append(intent['responses'])
    if intent['tag'] not in labels:
        labels.append(intent['tag'])
num_classes = len(labels)

lbl_encoder = LabelEncoder()
lbl_encoder.fit(training_labels)
training_labels = lbl_encoder.transform(training_labels)

vocab_size = 1000
embedding_dim = 16
max_len = 50
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

# Model Training

model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation='selu'))
model.add(Dense(16, activation='selu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam', metrics=['accuracy'])

model.summary()

epochs = 500
history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)

# to save the trained model
model.save("model/chat_model")

import pickle

# to save the fitted tokenizer
with open('model/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
# to save the fitted label encoder
with open('model/label_encoder.pickle', 'wb') as ecn_file:
    pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)

@csrf_exempt
def chatanswer(request):
    context = {}

    questext = request.GET['questext']
    import pickle

    file = open("./model/intents.json", encoding="UTF-8")
    data = json.loads(file.read())

    def chat3(inp):
        # load trained model
        model = keras.models.load_model('model/chat_model')

        # load tokenizer object
        with open('model/tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        # load label encoder object
        with open('model/label_encoder.pickle', 'rb') as enc:
            lbl_encoder = pickle.load(enc)

        # parameters
        max_len = 50

        # while True:
        print("User: ", end="")

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                                                          truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag'] == tag:
                txt1 = np.random.choice(i['responses'])
                print("ChatBot:" , txt1)

        return txt1

    anstext = chat3(questext)
    print(anstext)

    context['anstext'] = anstext
    context['flag'] = '0'

    return JsonResponse(context, content_type="application/json")