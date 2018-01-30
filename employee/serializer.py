class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('instructor_id', 'name', 'email', 'phone', 'date_of_joining', 'password', 'designation', 'room_no', 'school',)
        extra_kwargs = {'password': {'write_only': True}}
