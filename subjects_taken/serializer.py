class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class SubjectsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
