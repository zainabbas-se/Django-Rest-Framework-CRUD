from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transactions
from .serializers import TransactionsSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def get_transaction(request):
    queryset = Transactions.objects.all().order_by('-pk')

    serializer = TransactionsSerializer(queryset, many=True)

    return Response({
        'data': serializer.data,
    })


class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transactions.objects.all().order_by('-pk')
        serializer = TransactionsSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
        })

    def post(self, request):
        data = request.data
        serializer = TransactionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Transaction created successfully',
                'data': serializer.data,
            })
        else:
            return Response({
                'message': 'Data not saved',
                'error': serializer.errors,
            })

    def put(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                'message': 'Data not Update',
                'error': "id is Required",
            })
        transaction = Transactions.objects.get(id=data.get('id'))
        serializer = TransactionsSerializer(transaction, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Transaction has been updated successfully',
                'data': serializer.data,
            })
        else:
            return Response({
                'message': 'Data not saved',
                'error': serializer.errors,
            })

    def patch(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                'message': 'Data not Update',
                'error': "id is Required",
            })
        transaction = Transactions.objects.get(id=data.get('id'))
        serializer = TransactionsSerializer(transaction, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Transaction has been updated successfully',
                'data': serializer.data,
            })
        else:
            return Response({
                'message': 'Data not saved',
                'error': serializer.errors,
            })

    def delete(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                'message': 'Data not deleted',
                'error': 'id is required'
            })

        transaction = Transactions.objects.get(id=data.get('id'))
        transaction.delete()
        return Response({
            'message': 'Data deleted successfully',
        })


class loginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user_object = authenticate(username=username, password=password)
            if user_object:
                token, _ = Token.objects.get_or_create(user=user_object)
                return Response({
                    'status': True,
                    'data': {"Token": str(token)},
                })

        return Response({
            'status': False,
            'message': "Invalid Username or Password",
            'error': serializer.errors,
        })
