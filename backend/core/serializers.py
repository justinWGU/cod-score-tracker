from rest_framework import serializers
from .models import Match

# def create(self, validated_data):
#     return Comment.objects.create(**validated_data)
#
#
# def update(self, instance, validated_data):
#     instance.email = validated_data.get('email', instance.email)
#     instance.content = validated_data.get('content', instance.content)
#     instance.created = validated_data.get('created', instance.created)
#     instance.save()
#     return instance


# # .save() will create a new instance.
# serializer = CommentSerializer(data=data)
#
# # .save() will update the existing `comment` instance.
# serializer = CommentSerializer(comment, data=data)


# serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
# serializer.is_valid(raise_exception=True)
# # False
# serializer.errors
# # {'email': ['Enter a valid e-mail address.'], 'created': ['This field is required.']}

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['leftTeamScore', 'rightTeamScore']