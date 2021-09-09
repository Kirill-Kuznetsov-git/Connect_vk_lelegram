from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializers import MessageCreateSerializer, MessageUpdateSerializer


class MessageView(APIView):
    def get(self, request, vk_id):
        mess = Message.objects.get(vk_id=int(vk_id))
        serializer = MessageCreateSerializer(mess)
        return Response({"message": serializer.data})

    def post(self, request):
        data = request.data
        serializer = MessageCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_message = serializer.create(data)
            return Response({"status": "Success", "description": f"Message {saved_message} saved.",
                             "message": saved_message.to_json()})
        return Response({"status": "Error", "description": "Validate error."})

    def patch(self, request, vk_id):
        print("ASD")
        mess = Message.objects.get(vk_id=int(vk_id))
        data = request.data
        serializer = MessageUpdateSerializer(instance=mess, data=data)
        if serializer.is_valid(raise_exception=True):
            updated_message = serializer.update(mess, data)
            return Response({"status": "Success", "desription": f"Message {updated_message} updated.",
                             "message": updated_message.to_json()})
        return Response({"status": "Error", "description": "Validate error."})
