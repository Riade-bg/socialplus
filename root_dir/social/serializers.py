from rest_framework import serializers
from users.models import Profile

class SearchSerializers(serializers.ModelSerializer):
	class Meta:
	    model = Profile
	    fields = ('user', 'avatar')
