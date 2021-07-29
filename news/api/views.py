from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Articles,Journalists
from news.api.serializers import ArticleSerializers,JournalitsSerializers
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class Journalists_list_API_VIEW(APIView):
    def get(self,request):
        journalists=Journalists.objects.all()
        serializers=JournalitsSerializers(journalists,many=True,context={'request': request})
        return Response(serializers.data)
    
    def post(self,request):
        serializers=JournalitsSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class Article_list_API_VIEW(APIView):
    def get(self,request):
        articles=Articles.objects.filter(is_active=True)
        serializers=ArticleSerializers(articles,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=ArticleSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)




class Article_Detail_API_VIEW(APIView):

    def get_object(self,pk):
        articles=get_object_or_404(Articles,pk=pk)
        return articles

    def get(self,request,pk):
        article=self.get_object(pk=pk)
        serializers=ArticleSerializers(article)
        return Response(serializers.data)
    def put(self,request,pk):
        article=self.get_object(pk=pk)
        serializers=ArticleSerializers(article,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        article=self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















@api_view(['GET','POST'])
def articles_list_create_aiw_view(request):

    if request.method=="GET":
        articles=Articles.objects.filter(is_active=True)    
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer= ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def articles_detail_view(request,pk):
    try:
        articles_inststance=Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method=="GET":
        serializers=ArticleSerializers(articles_inststance)
        return Response(serializers.data)
    if request.method=="PUT":
        serializers=ArticleSerializers(articles_inststance,data=request.data)
        if serializers.is_valid():
            return Response(serializers.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        articles_inststance.delete()
        return Response({
            'errors':{
                    'code' : 204,
                    'message': f"Article has been deleted with ({id})"
                }
        }
            ,status=status.HTTP_204_NO_CONTENT)