class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'
