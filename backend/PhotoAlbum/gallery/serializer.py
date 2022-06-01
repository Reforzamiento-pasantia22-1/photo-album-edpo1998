# Django

# Django RestFramework
from rest_framework import serializers

# Models
from gallery import models as gallery_models
from django.contrib.auth import get_user_model



class ImageSerializer(serializers.ModelSerializer):
    '''
        Class to serialize the image model
        ...

        Nested Classes
        --------------
        Meta:
            Clas with customize model
    '''
    class Meta:
        '''
            Attributes
            ----------
            model:
                model to use in customization
            fields:
                attributes to use in the configuration
        '''
        model = gallery_models.Image
        fields = '__all__'

    

class AlbumSerializer(serializers.ModelSerializer):
    '''
        Class to serialize the Album model
        ...

        Attributes
        ----------
        images:
            Serializer relation for related_name

        Nested Classes
        --------------
        Meta:
            Clas with customize model
    '''
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        '''
            Attributes
            ----------
            model: Album
                model to use in customization
            fields: []
                attributes to use in the configuration
        '''
        model = gallery_models.Album
        fields = ["user","id",'album_name',"images"]

class UserSerializer(serializers.ModelSerializer):
    '''
        Class to serialize the User model
        ...

        Attributes
        ----------
        gallery:
            Serializer relation for related_name

        Nested Classes
        --------------
        Meta:
            Clas with customize model
    '''
    #gallery = AlbumSerializer(many=True)
    
    class Meta:
        '''
            Attributes
            ----------
            model: User
                model to use in customization
            fields: []
                attributes to use in the configuration
        '''
        model = get_user_model()
        fields = ['username','name', 'surname','email']

class UsersGallery(UserSerializer):
    gallery = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id','gallery']