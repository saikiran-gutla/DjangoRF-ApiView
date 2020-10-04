from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from testapp.serializer import EmployeeSerializer
from testapp.models import Employee
from rest_framework.filters import SearchFilter


# Create your views here.
# class EmployeeListApiView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeUpdateApiView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# LIST , SEARCH , CREATE API VIEW
class EmployeeCreateApiView(ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.query_params.get('ename', None)
        print(f"NAME : {name}")
        if name is not None:
            qs = qs.filter(ename=name)
            filter_backends = [SearchFilter]
            search_fields = ['ename']

        return qs


from rest_framework import filters


class UserListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['esal']


class UserListViewFilter(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['ename']
    ordering = ['esal']


class EmployeeRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
