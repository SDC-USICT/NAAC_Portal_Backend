from rest_framework import serializers

from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('instructor_id', 'name', 'email', 'phone', 'date_of_joining', 'password', 'designation', 'room_no', 'school')
        extra_kwargs = {'password': {'write_only': True}}
