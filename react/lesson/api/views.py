from lesson.api.serializers import PostSerializer
from lesson.models import Post
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET', 'POST'])
def post_list(request, format=None):
    if request.method == 'GET':
        employeis = Post.objects.all()
        serializer = PostSerializer(employeis, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('success', safe=False)
        return JsonResponse('errors', safe=False)

@api_view(['GET'])
def post_detail(request, pk):
    employee = Post.objects.get(id=pk)
    serializer = PostSerializer(employee)

    return JsonResponse(serializer.data, safe=False)