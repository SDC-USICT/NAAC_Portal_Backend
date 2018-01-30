class Serializer(serializers.ModelSerializer):
    class Meta:
        model = GuestLecture
        fields = '__all__'
