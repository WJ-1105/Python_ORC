from django.shortcuts import render
from index.models import image_to_json
import pytesseract
from PIL import Image
import re
from string import punctuation
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import image_to_jsonSerializer
from rest_framework.parsers import FileUploadParser
# from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser ,FormParser
from rest_framework.decorators import parser_classes

from rest_framework.views import APIView
from rest_framework import status



class index(APIView):
	
	def get(self, request):
		image_to_jsons = image_to_json.objects.all()
		serializer = image_to_jsonSerializer(image_to_jsons,many = True)
		return Response(serializer.data)
	parser_classes = (MultiPartParser, FormParser)
	def post(self, request, format=None):
		img  = request.data.get("movie_image")
		print(img)
		img1 = Image.open(img)


		text = pytesseract.image_to_string(img1)
		text = re.sub(r"[%s]+" %punctuation, "",text)
		text = re.sub(r'[0-9]+', '', text)
		text = re.sub(r'\n', '', text)
		text = re.sub(r'\x0c', '', text)
		text = re.sub(r' ', '', text)
		# text = re.sub(r'\n\x0c', '', text)
		text = list(text)
		# text = ["a","b"]
		dic = {}
		dic['content']=text
		# json1 = json.dumps(dic)
		


		tmp = {
		"movie_image" : img,
		"data" : dic

		}

		serializer = image_to_jsonSerializer(data=tmp)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED) 
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		# print(serializer.errors)
			# serializer.save()
		# else:
		# 	print("errorrrrrrrrrrrrrr")

		# return Response(serializer.data,status=status.HTTP_201_CREATED) 



# Create your views here.
# @api_view(['GET','POST'])
# @parser_classes([MultiPartParser,FormParser])
# def index(request, format=None):
# 	if request.method == 'GET':
# 		image_to_jsons = image_to_json.objects.all()
# 		serializer = image_to_jsonSerializer(image_to_jsons,many = True)
# 		return Response(serializer.data)
# 	elif request.method == 'POST':
# 		# image_tuple = image_to_json()

# 		img  = request.data.get('movie_image')
# 		img1 = Image.open(img)


# 		text = pytesseract.image_to_string(img1)
# 		text = re.sub(r"[%s]+" %punctuation, "",text)
# 		text = re.sub(r'[0-9]+', '', text)
# 		text = re.sub(r'\n', '', text)
# 		text = re.sub(r'\x0c', '', text)
# 		text = re.sub(r' ', '', text)
# 		# text = re.sub(r'\n\x0c', '', text)
# 		text = list(text)
# 		dic = {}
# 		dic['content']=text
# 		# json1 = json.dumps(dic)
		


# 		tmp = {
# 		"movie_image" : img,
# 		"data" : dic

# 		}

# 		serializer = image_to_jsonSerializer(data=tmp)
# 		if serializer.is_valid():
# 			serializer.save()
# 		else:
# 			print(serializer.errors)
# 		# print(serializer.errors)
# 			# serializer.save()
# 		# else:
# 		# 	print("errorrrrrrrrrrrrrr")

# 		return Response(serializer.data) 


		# image_tuple = image_to_json(movie_image = img , data = dic)



		
		# image_tuple.save()


		# context = {'json_val': image_to_json.objects.all().order_by('-id')[0]}


		# return render(request, 'index/index.html',context)



		