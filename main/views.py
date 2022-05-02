import json
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow 
from tensorflow import keras
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from django.http import HttpResponse, JsonResponse

def index(request):
	context={}
	return render(request, 'main/index.html',context)

def about(request):
	return render(request, 'main/about.html')

@csrf_exempt
def chatanswer(request):
    context = {}

    questext = request.GET['questext']

    import pickle

    file = open(f"./static/intents.json", encoding="UTF-8")
    data = json.loads(file.read())

    def chat3(inp):
        # load trained model
        model = keras.models.load_model('static/chat_model')

        # load tokenizer object
        with open('static/tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        # load label encoder object
        with open('static/label_encoder.pickle', 'rb') as enc:
            lbl_encoder = pickle.load(enc)

        # parameters
        max_len = 50

        # while True:
        print( "User: ", end="")

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

    return JsonResponse(context,content_type="application/json")