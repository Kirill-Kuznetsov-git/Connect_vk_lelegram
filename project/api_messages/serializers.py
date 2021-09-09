from rest_framework import serializers

from .models import Message


class MessageCreateSerializer(serializers.Serializer):
    vk_id = serializers.IntegerField(required=True)
    vk_name_author = serializers.CharField(max_length=100, required=True)
    vk_id_author = serializers.IntegerField(required=True)
    text_question = serializers.CharField(max_length=1000, required=True)

    telegram_id_who_answered = serializers.IntegerField(required=False)
    telegram_name_author = serializers.CharField(max_length=100, required=False)
    telegram_id = serializers.IntegerField(required=False)
    text_answer = serializers.CharField(max_length=1000, required=False)

    def create(self, validate_data):
        return Message.objects.create(**{"vk_id": validate_data.get("vk_id"),
                                         "vk_name_author": validate_data.get("vk_name_author"),
                                         "vk_id_author": validate_data.get("vk_id_author"),
                                         "text_question": validate_data.get("text_question")})


class MessageUpdateSerializer(serializers.Serializer):
    telegram_id_who_answered = serializers.IntegerField(required=False)
    telegram_name_author = serializers.CharField(max_length=100, required=False)
    telegram_id = serializers.IntegerField(required=False)
    text_answer = serializers.CharField(max_length=1000, required=False)

    def update(self, instance, validated_data):
        instance.telegram_id_who_answered = validated_data.get('telegram_id_who_answered',
                                                               instance.telegram_id_who_answered)
        instance.telegram_name_author = validated_data.get('telegram_name_author', instance.telegram_name_author)
        instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
        instance.text_answer = validated_data.get('text_answer', instance.text_answer)
        instance.save()
        return instance
