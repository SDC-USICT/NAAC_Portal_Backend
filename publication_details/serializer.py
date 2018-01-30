class JournalPapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class BookChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
