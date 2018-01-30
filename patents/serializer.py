class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patents
        fields = '__all__'
