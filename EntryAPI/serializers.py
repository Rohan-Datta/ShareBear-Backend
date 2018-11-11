from rest_framework import serializers
from EntryAPI.models import Entry
from rest_framework import serializers
from UserAPI.models import User

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('name','posted_by','created_at','updated_at','entry_type', 'tags')