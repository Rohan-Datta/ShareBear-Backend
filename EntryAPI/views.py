from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from EntryAPI.models import Entry
from EntryAPI.serializers import EntrySerializer
from UserAPI.models import User
from UserAPI.serializers import UserSerializer
from django.http import Http404

# Lists all entries or creates a new one
class EntryList(APIView):
    def get(self, request):
    	entries = Entry.objects.all()

    	serializer = EntrySerializer(entries, many=True)
    	return Response(serializer.data)

    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Similar to UserAPI
class EntryDetail(APIView):

    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = EntrySerializer(snippet)

        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = EntrySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)