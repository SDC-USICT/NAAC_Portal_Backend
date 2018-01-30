class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = '__all__'
