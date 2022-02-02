from datetime import datetime
from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status, authentication, permissions
from django.contrib.auth.models import update_last_login
from django.db.models import Sum
from .models import Post, PostLikes, Profile

from .serializers import PostSerializer, UserSerializer
from .authentication import BearerAuthentication


@api_view(['POST'])
def SignUp(request):
    if not request.user.is_authenticated:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return redirect("login/")

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([permissions.IsAuthenticated])
def createPost(request):
    updated_data = request.data.copy()
    updated_data.update({'author':request.user.id})

    serializer = PostSerializer(data=updated_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([permissions.IsAuthenticated])
def likePost(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    if PostLikes.objects.filter(post=post, user=request.user).exists():
        postLike = PostLikes.objects.filter(post=post, user=request.user).first()
        postLike.count +=1
        postLike.liked = datetime.now()
        postLike.save()
    else:
        post.likes.add(request.user)
    context = {"message":"Post liked"}
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([permissions.IsAuthenticated])
def unlikePost(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    post.likes.remove(request.user)
    context = {"message":"Post unliked"}
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([BearerAuthentication])
@permission_classes([permissions.IsAuthenticated])
def analitics(request):
    date_from = request.GET.get('date_from','')
    date_to = request.GET.get('date_to', '')
    
    likes = (PostLikes.objects
        .filter(user=request.user, liked__range=[date_from, date_to])
        .values("liked")
        .annotate(count_sum=Sum("count"))
    )
    context = {"message":date_from, "message2": date_to, "likes":likes}

    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([BearerAuthentication])
@permission_classes([permissions.IsAuthenticated])
def lastLogin(request):
    context = {
        "last_login" : request.user.last_login,
        "last_activity" : Profile.objects.get(user__id=request.user.id).last_activity
    }
    return Response(context, status=status.HTTP_200_OK)

class LoginToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=result.data['token'])
        update_last_login(None, token.user)
        return result
