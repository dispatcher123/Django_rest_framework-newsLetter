from django.db.models import fields
from rest_framework import serializers
from rest_framework.settings import reload_api_settings
from news.models import Articles, Journalists
from datetime import datetime
from datetime import date
from django.utils.timesince import timesince



class ArticleSerializers(serializers.ModelSerializer):
    time_pub_time=serializers.SerializerMethodField()
    class Meta:
        model= Articles
        fields="__all__"
        read_only_fields=['id','created_date','updated_date']

    def get_time_pub_time(self,object):
        time=datetime.now()
        pub_date=object.published_date
        if object.is_active == True:
            time_delta=timesince(pub_date,time)
            return time_delta
        else:
            return ('Thats Article is not active!')

    def validate_published_date(self,value):
        today=date.today()
        if today < value:
            raise serializers.ValidationError('Please enter a correct date')
        return value


class JournalitsSerializers(serializers.ModelSerializer):

    #articles=ArticleSerializers(many=True,read_only=True)

    articles=serializers.HyperlinkedRelatedField(
        read_only=True,
        many=True,
        view_name='detail_article',
        
    )

    class Meta:
        model= Journalists
        fields="__all__"
        



####### BASIC SERIALIZERS
class ArticleDefaultSerializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    author=serializers.CharField()
    title=serializers.CharField()
    body=serializers.CharField()
    context=serializers.CharField()
    city=serializers.CharField()
    published_date=serializers.DateField()
    created_date=serializers.DateTimeField(read_only=True)
    updated_date=serializers.DateTimeField(read_only=True)
    is_active=serializers.BooleanField()



    def create(self, validated_data ):
        return Articles.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.author=validated_data.get('author',instance.author)
        instance.title=validated_data.get('title',instance.title)
        instance.body=validated_data.get('body',instance.body)
        instance.context=validated_data.get('context',instance.context)
        instance.city=validated_data.get('city',instance.city)
        instance.published_date=validated_data.get('published_date',instance.published_date)
        instance.is_active=validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance


    def validate(self,data):
        if data['title'] == data['body']:
            raise serializers.ValidationError('Tittle and Content are same')
        return data

    def validate_title(self,value):
        if len(value) < 20:
            raise serializers.ValidationError(f'Title should be min 20 characters. You wrote {len(value)} character.')
        return value