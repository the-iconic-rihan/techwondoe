from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from company.models import Company
from company.serializers import CompanySerializer
import uuid


# class companyList(ListCreateAPIView):
#         if id:
#             # If an id is provided in the GET request, retrieve the Company by that id
#             try:
#                 # Check if the Company the user wants to update exists
#                 queryset = Company.object.get(uuid)
#             except Company.DoesNotExist:
#                 # If the Company does not exist, return an error response
#                 return Response({'errors': 'This User does not exist.'}, status=400)
#             # Serialize Company from Django queryset object to JSON formatted data
#             company_serializer = CompanySerializer(queryset)
#         else:
#             # Get all Company from the database using Django's model ORM
#             queryset = Company.objects.all()
#             # Serialize list of Company from Django queryset object to JSON formatted data
#             company_serializer = CompanySerializer(queryset, many=True)
#         # Return a HTTP response object with the list of Company as JSON
#         return Response(company_serializer.data)


class collectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            # If an id is provided in the GET request, retrieve the Company by that id
            try:
                # Check if the Company the user wants to update exists
                queryset = Company.objects.get(companyId=id)
            except Company.DoesNotExist:
                # If the Company does not exist, return an error response
                return Response({'errors': 'This User does not exist.'}, status=400)
            # Serialize Company from Django queryset object to JSON formatted data
            company_serializer = CompanySerializer(queryset)
        else:
            # Get all Company from the database using Django's model ORM
            queryset = Company.objects.all()
            # Serialize list of Company from Django queryset object to JSON formatted data
            company_serializer = CompanySerializer(queryset, many=True)
        # Return a HTTP response object with the list of Company as JSON
        return Response(company_serializer.data)

    def post(self, request, *args, **kwargs):
        # Retrieve the

        data = {
            'uuId': request.data.get('uuId'),
            'companyName': request.data.get('companyName'),
            'companyCeo': request.data.get('companyCeo'),
            'companyAddress': request.data.get('companyAddress')
        }
        # Serialize Company from Django data variable to JSON formatted data

        company_serializer = CompanySerializer(data=data, partial=True)
        if company_serializer.is_valid():
            company_serializer.save()
            # Return a HTTP response object with the Company JSON
            return Response(company_serializer.data, status=status.HTTP_200_OK)
        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id:
            count = Company.objects.get(uuId=id).delete()
            return Response({'message': '{} Company were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            count = Company.objects.all().delete()
            return Response({'message': '{} Company were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

    def get_by_name(self, request, name=None):
        if name:
            try:
                company = Company.objects.filter(companyName=name)
                company_serializer = CompanySerializer(company, many=True)
                return Response(company_serializer.data)
            except Company.DoesNotExist:
                # If the Company does not exist, return an error response
                return Response({'errors': 'This Company does not exist.'}, status=400)
        else:
            company = Company.objects.all()
            company_serializer = CompanySerializer(company, many=True)
        return Response(company_serializer.data)


# def companyDetails(request, id=0):
#     if request == "GET":
#         company = Company.objects.all()
#         # converting data into json format using serializer
#         company_serializer = CompanySerializer(company, many=True)
#         # safe = false = values passing are in valid format and its ok to get it if any issues in data.
#         return HttpResponse(company_serializer.data)
#     elif request.method == 'Post':
#         # parsing the request
#         company_data = JSONParser().parse(request)
#         # converting json data to model
#         company_serializer = CompanySerializer(data=company_data)
#         if company_serializer.is_valid():
#             company_serializer.save()
#             # Return a HTTP response object with the company JSON
#             return HttpResponse(company_serializer.data, status=status.HTTP_200_OK)
#         return HttpResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PUT':
#         company_data = JSONParser().parse(request)
#         # capturing the exiting record using UUID
#         company = Company.objects.get(uuId=company_data["uuId"])
#         company_serializer = CompanySerializer(company, data=company_data)
#         if company_serializer.is_valid():
#             company_serializer.save()
#             return HttpResponse(company_serializer.data, status=status.HTTP_200_OK)
#         return HttpResponse(company_serializer.errors, status=status.HTTP_302_FOUND)
#     elif request.method == "DELETE":
#         if id:
#             company = Company.objects.get(uuId=id)
#             company.delete()
#             return HttpResponse({'message': '{} Company were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#         else:
