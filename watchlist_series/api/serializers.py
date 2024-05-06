from rest_framework import serializers
from watchlist_series.models import Series


class SeriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    tags = serializers.CharField()
    is_watched = serializers.BooleanField()
    ott = serializers.CharField()

    def create(self, validated_data):
        return Series.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.tags = validated_data.get("tags", instance.tags)
        instance.is_watched = validated_data.get("is_watched", instance.is_watched)
        instance.ott = validated_data.get("ott", instance.ott)
        instance.save()
        return instance
