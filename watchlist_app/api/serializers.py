from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude =('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True,read_only = True)
    # len_names = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = ('id', 'title','storyline', 'active', 'created','platform','review')
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = ('id', 'name', 'about', 'website','watchlist')
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

# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         WatchList.objects.create(validated_data)
    
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

