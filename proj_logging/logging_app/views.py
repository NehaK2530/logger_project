from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostCreateSerializer, PostUpdateSerializer
from .models import Post
from django.shortcuts import get_object_or_404
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


error_logger = logging.getLogger('error_logger')
success_logger = logging.getLogger('success_logger')

class PostAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get(self,request):
        try:
            posts = Post.objects.all()
            serializer = PostCreateSerializer(posts, many=True)
            success_logger.info('Posts fetched successfully')
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f'there is an error fetching the posts')
            return Response(data={'details':'There is an error fetching the posts'},status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = PostCreateSerializer(data=request.data, context={'request': request})    
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f'Post with id {serializer.data.get("id")} created successfully')
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_logger.error(f'Error saving the data {serializer.errors}')
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        