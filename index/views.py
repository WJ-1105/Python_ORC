from django.shortcuts import render
from index.models import image_to_json
import pytesseract
from PIL import Image
import re
from string import punctuation
import json


# Create your views here.

def index(request):
	if request.method == 'GET':
		return render(request, 'index/index.html')
	elif request.method == 'POST':
		# image_tuple = image_to_json()
		img=  request.FILES.get('img')
		img1 = Image.open(img)


		text = pytesseract.image_to_string(img1)
		text = re.sub(r"[%s]+" %punctuation, "",text)
		text = re.sub(r'[0-9]+', '', text)
		text = re.sub(r'\n', '', text)
		text = re.sub(r'\x0c', '', text)
		text = re.sub(r' ', '', text)
		# text = re.sub(r'\n\x0c', '', text)
		text = list(text)
		dic = {}
		dic['content']=text
		# json1 = json.dumps(dic)
		


		image_tuple = image_to_json(movie_image = img , data = dic)

		
		image_tuple.save()


		context = {'json_val': image_to_json.objects.all().order_by('-id')[0]}


		return render(request, 'index/index.html',context)



		