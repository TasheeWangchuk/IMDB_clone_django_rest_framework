from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # len_names = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'active', 'len_names')
        
    # def get_len_names(self,object):
    #     return len(object.name)
        
    # def validate_name(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Name must be at least 5 characters long.")
    #     return value

    # def validation(self,value):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError("Title and description must be different.")
    #     else:
    #         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         Movie.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
        
#     def validate_name(self, value):
#         if len(value) < 5:
#             raise serializers.ValidationError("Name must be at least 5 characters long.")
#         return value
    
#     def validation(self,value):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and description must be different.")
#         else:
#             return value

