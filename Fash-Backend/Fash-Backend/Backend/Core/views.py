import os
from django.http import JsonResponse
from rest_framework.views import APIView
import numpy as np


from .models import UserModel, HomeModel, FirstScreenModel,SecondScreenModel,ThirdScreenModel,Output
from .serializer import HomeSerializer, SecondScreenSerializer, ThirdScreenSerializer
from Backend.settings import MEDIA_ROOT, MEDIA_URL
from .ExtractColor import extract_color
import cv2
from PIL import Image

# from Tools.ExpertSys import *
from .searchExpertSystem import Search
from .QueryDatabase import Quary
from .SearchAll import searchAll
from .CNNModel import modelCNN




class UserLogIn(APIView):
    def post(self, request, format=None):
        try:
            queryset = UserModel.objects.filter(

                Username=request.data["Username"], Password=request.data["Password"])


            if queryset:
                return JsonResponse({
                    "Code": 200,
                    "USERID": str(queryset[0].USERID)
                })
        except Exception as e:
            return JsonResponse({
                "Code": 404,
                "Message": str(e)
                    # "UserName or Password is Wrong"
            })


class UserSignUp(APIView):
    def post(self, request, format=None):

        try:
            username = request.data["Username"]
            print(username)
            password = request.data["Password"]
            age = request.data["Age"]
            skinColor = request.data["SkinColor"]
            gender = request.data["Gender"]
            ins = UserModel.objects.create(
                Username=username, Password=password, Gender=gender, Age=age, SkinColor=skinColor)
            ins.save()
            return JsonResponse({
                "Code": 200,
                "USERID": str(ins.USERID)
            })
        except Exception as e:
            return JsonResponse({
                "Code": 400,
                "Message": "Error In SignUp",
                "Details": str(e)
            })




class homeView(APIView):
    def post(self, request, format=None):
        try:
            serializer = HomeSerializer(data=request.data)
            if serializer.is_valid(True):
                ins = serializer.save()
            db_img_path = str(ins.Image)
            ImagePath = os.path.join(MEDIA_ROOT, db_img_path)
            print(ImagePath)
            user = serializer.data["USERID"]
            print(user)
            return JsonResponse({
                "Code": 200,
                "USERID": str(user),
                "Image": os.path.join(MEDIA_URL, db_img_path)

            })
        except Exception as e:
            return JsonResponse({
                "Code": 400,
                "Message": "Error In Post Home View",
                "Detaile": str(e)
            })


class FirstScreenView(APIView):
    def post(self, request, format=None):
        try:
            userid = request.data["USERID"]
            occasion = request.data["Occasion"]
            personType = request.data["PersonType"]
            ins = FirstScreenModel.objects.create(
                USERID=userid, Occasion=occasion, PersonType=personType)
            ins.save()
            return JsonResponse({
                "Code": 200,
                "USERID": str(ins.USERID),
            })
        except Exception as e:
            return JsonResponse({
                "Code": 400,
                "Message": "Error In Post Home View",
                "Detaile": str(e)
            })
    def get(self, request, format=None):
        
        try:
            user_id = request.GET["USERID"]
            queryset1 = HomeModel.objects.filter(
                USERID=user_id)
            queryset2= UserModel.objects.filter(
                USERID=user_id)
            queryset3 = FirstScreenModel.objects.filter(
                USERID=user_id)

            if queryset1 :
                for i in range(len(queryset1)):
                    print(i, queryset1[i].USERID),

                result ={
                "Code": 200,
                "USERID":str(queryset1[len(queryset1)-1].USERID),
                "Season": str(queryset1[len(queryset1)-1].Season),
                "Age": str(queryset2[len(queryset2)-1].Age),
                "Gender": str(queryset2[len(queryset2)-1].Gender),
                "SkinColor":str(queryset2[len(queryset2)-1].SkinColor),
                "Occasion":str(queryset3[len(queryset3)-1].Occasion),
                "PersonType":str(queryset3[len(queryset3)-1].PersonType)
                }
                # print(result)
                search1_= Search()
                res = search1_.AllresultFirst(result)
                qurey = Quary()
                print(len(res))
                search=searchAll()
                paths=search.selectfromDataAndRule(qurey,res,user_id)
                print("trtrtrtttttttttttttttttrrrrrrrrrrrrrr")

                return JsonResponse(paths)
        except Exception as e:
            return JsonResponse({
                "Code": 404,
                "Message": e
            })



class SecondScreenView(APIView):
    def post(self, request, format=None):
        try:
            serializer = SecondScreenSerializer(data=request.data)
            if serializer.is_valid(True):
                ins = serializer.save()

            user = ins.USERID
            return JsonResponse({
                "Code": 200,
                "USERID": str(user),
            })
        except Exception as e:
            return JsonResponse({
                "Code": 400,
                "Message": "Error In Post Home View",
                "Detaile": str(e)
            })


class ThirdScreenView(APIView):
    def post(self, request, format=None):
        try:
            serializer = ThirdScreenSerializer(data=request.data)
            if serializer.is_valid(True):
                ins = serializer.save()
            db_img_path = str(ins.Image)
            ImagePath = os.path.join(MEDIA_ROOT, db_img_path)

            user = serializer.data["USERID"]
            return JsonResponse({
                "Code": 200,
                "USERID": str(user),
                "Image": os.path.join(MEDIA_URL, db_img_path)

            })
        except Exception as e:
            return JsonResponse({
                "Code": 400,
                "Message": "Error In Post Home View",
                "Detaile": str(e)
            })

class userInformation(APIView):
    def get(self, request, format=None):
        try:
            queryset1 = HomeModel.objects.filter(
                            USERID=request.data["USERID"])
            if queryset1:
                for i in range(len(queryset1)):
                    print(queryset1[i].Season)
                return JsonResponse({
                "Code": 200,
                    "USERID": str(queryset1[0].USERID),
                    "Season": str(queryset1[0].Season)


            })
        except Exception as e:
            return JsonResponse({
                "Code": 400,
                "Message": "Error In Post Home View",
                "Detaile": str(e)
            })


class selectimagefirst(APIView):
    def get(self, request, format=None):

        try:
            user_id = request.GET["USERID"]
            print(user_id)
            queryset1 = HomeModel.objects.filter(
                USERID=user_id)
            queryset2 = UserModel.objects.filter(
                USERID=user_id)
            queryset3 = FirstScreenModel.objects.filter(
                USERID=user_id)

            if queryset1 and queryset2 and queryset3:


                result = {
                    "Code": 200,
                    "USERID": str(queryset1[len(queryset1) - 1].USERID),
                    "Season": str(queryset1[len(queryset1) - 1].Season),
                    "Age": str(queryset2[len(queryset2) - 1].Age),
                    "Gender": str(queryset2[len(queryset2) - 1].Gender),
                    "SkinColor": str(queryset2[len(queryset2) - 1].SkinColor),
                    "Occasion": str(queryset3[len(queryset3) - 1].Occasion),
                    "PersonType": str(queryset3[len(queryset3) - 1].PersonType)
                }

                search1_ = Search()
                res1 = search1_.AllresultFirst(result)
                qurey = Quary()
                search = searchAll()
                paths = search.selectfromDataAndRule(qurey, res1, user_id)
                print(paths)

                return JsonResponse(paths)



        except Exception as e:
            return JsonResponse({
                "Code": 404,
                "Message": e
            })


class selectimagesecind(APIView):
    def get(self, request, format=None):
        try:
            user_id = request.GET["USERID"]
            queryset1 = HomeModel.objects.filter(
                USERID=user_id)
            queryset2 = UserModel.objects.filter(
                USERID=user_id)
            queryset3 = SecondScreenModel.objects.filter(
                USERID=user_id)

            namecloth=""
            if queryset1:
                for i in range(len(queryset1)):
                    print(i, queryset1[i].USERID),
                namecloth=str(queryset3[len(queryset3) - 1].ClotheName)
                print("jjjjjjjjjjjjjjjjjj ",namecloth)
                result = {
                    "Code": 200,
                    "USERID": str(queryset1[len(queryset1) - 1].USERID),
                    "Season": str(queryset1[len(queryset1) - 1].Season),
                    "Age": str(queryset2[len(queryset2) - 1].Age),
                    "Gender": str(queryset2[len(queryset2) - 1].Gender),
                    "SkinColor": str(queryset2[len(queryset2) - 1].SkinColor),
                    "Occasion": str(queryset3[len(queryset3) - 1].Occasion),
                    "PersonType": str(queryset3[len(queryset3) - 1].PersonType),
                    "ClotheName": str(queryset3[len(queryset3) - 1].ClotheName),
                    "Type": str(queryset3[len(queryset3) - 1].Type),
                    "Color": str(queryset3[len(queryset3) - 1].Color),
                }
                print(result)

                search1_ = Search()
                res = search1_.AllresultSecond(result)
                print(res)
                qurey = Quary()
                search = searchAll()
                paths = search.selectfromDataAndRuleSecond(qurey,namecloth,res, user_id,namecloth)


            return JsonResponse(paths)



        except Exception as e:
            return JsonResponse({
                "Code": 404,
                "Message": e
            })


class selectimagethird(APIView):
    def get(self, request, format=None):
        try:
            #
            user_id = request.GET["USERID"]
            queryset1 = HomeModel.objects.filter(
                USERID=user_id)
            queryset2 = UserModel.objects.filter(
                USERID=user_id)
            queryset3 = ThirdScreenModel.objects.filter(
                USERID=user_id)

            pathimage=""
            namecloth = ""
            colorClothes=""

            if queryset3:
                pathimage = str(queryset3[len(queryset3) - 1].Image)

            modelCNN1 = modelCNN()
            obj = extract_color("C:/Users/bayan/OneDrive/Desktop/Fash-Backend/media/"+pathimage)

            if queryset1:

                open1 = modelCNN1.open("C:/Users/bayan/OneDrive/Desktop/Fash-Backend/media/"+pathimage)
                value=modelCNN1.run_example(open1)
                namecloth=modelCNN1.nameclothes(value)
                print("tttttttddddddddddddddddddddddd  ",namecloth)
                colorClothes=obj.color()
                print("tttttttddddddddddddddddddddddd  ", colorClothes)
                for i in range(len(queryset1)):
                    print(i, queryset1[i].USERID),
                # namecloth = str(queryset3[len(queryset3) - 1].ClotheName)
                result = {
                    "Code": 200,
                    "USERID": str(queryset1[len(queryset1) - 1].USERID),
                    "Season": str(queryset1[len(queryset1) - 1].Season),
                    "Age": str(queryset2[len(queryset2) - 1].Age),
                    "Gender": str(queryset2[len(queryset2) - 1].Gender),
                    "SkinColor": str(queryset2[len(queryset2) - 1].SkinColor),
                    "Occasion": str(queryset3[len(queryset3) - 1].Occasion),
                    "PersonType": str(queryset3[len(queryset3) - 1].PersonType),
                    "ClotheName": str(namecloth),
                    "Color": str(colorClothes)
                }
                print(result)

                search1_ = Search()
                res = search1_.AllresultThird(result)
                qurey = Quary()
                print(res)
                print(len(res))
                search = searchAll()
                paths = search.selectfromDataAndRuleThird(qurey, res, user_id, namecloth,pathimage)
                # print("trtrtrtttttttttttttttttrrrrrrrrrrrrrr")

            return JsonResponse(paths)



        except Exception as e:
            return JsonResponse({
                "Code": 404,
                "Message": e
            })



