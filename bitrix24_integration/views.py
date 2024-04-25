from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer
from .models import NameWoman, NameMan


class WebhookView(APIView):
    """
    Пример запроса:
    ```
    {
        "contact_id": 123,
        "name": "John Doe"
    }
    ```
    """

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            contact_id = data.get('contact_id')
            name = data.get('name')

            # Поиск контакта по contact_id
            contact = Contact.objects.get(contact_id=contact_id)

            # Поиск имени в таблицах names_woman и names_man
            if NameWoman.objects.filter(name=name).exists():
                contact.gender = 'female'
            elif NameMan.objects.filter(name=name).exists():
                contact.gender = 'male'
            else:
                contact.gender = 'No gender'

            # Обновление данных контакта
            contact.name = name
            contact.save()

            serializer = ContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
