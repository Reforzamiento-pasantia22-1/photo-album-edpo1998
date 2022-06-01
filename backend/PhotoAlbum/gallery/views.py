# Django
from django.contrib.auth import get_user_model
from django.db.models import Q

# Django RestFramework
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets ,status

# apps
from gallery import serializer as serializer_gallery
from gallery import models as models_gallery
from gallery.template import TemplateResponse




class UsersViewSet(viewsets.ModelViewSet):
    '''
        class for the view and presentation of data 
        in django rest framework of the Users model

        Attributes
        ----------
        queryset: QuerySet of User model
            query set of users to serialize 
        serializer_class: UserSerializer
            serializer to present and manipulate the data
    '''
    queryset = get_user_model().objects.all()
    serializer_class = serializer_gallery.UserSerializer





class AlbumViewSet(viewsets.ModelViewSet):
    '''
        class for the view and presentation of data 
        in django rest framework of the Album model

        Attributes
        ----------
        queryset: QuerySet of Album model
            query set of albums to serialize 
        serializer_class: AlbumSerializer
            serializer to present and manipulate the data
        
        Methods
        -------
        list_Images_Album:
            return the list of images of a certain album

    '''
    queryset = models_gallery.Album.objects.all()
    serializer_class = serializer_gallery.AlbumSerializer

    @action(detail=False, methods=['GET'], name='list_Images_Album')
    def list_Images_Album(self,request, pk=None):
        """
            Parameters
            ----------
                request
                    In it will be the query params of the user id and the name of the album
                pk
                    does not receive an id Album 
        """
        #http://127.0.0.1:8000/gallery/albums/list_Images_Album/?id=1&name=Favoritos
        user_id = request.query_params.get('id')
        album_name = request.query_params.get('name')

        if user_id and album_name:
            repertorie =models_gallery.Album.objects.get(Q(user=user_id.rstrip()) | Q(album_name=album_name.rstrip()))
            serializer = self.serializer_class(repertorie, many=False)
            response = TemplateResponse(
                                status=status.HTTP_200_OK,error=False,
                                message="Album %s"%serializer.data["album_name"],
                                body=serializer.data["images"])

            return Response(response.getResponse())

        response = TemplateResponse(
                                status=status.HTTP_400_BAD_REQUEST,error=True,
                                message="No se especificaron datos",body=[])
        return Response(response.getResponse())





class ImageViewSet(viewsets.ModelViewSet):
    '''
        class for the view and presentation of data 
        in django rest framework of the Image model

        Attributes
        ----------
        queryset: QuerySet of Image model
            query set of images to serialize 
        serializer_class: ImageSerializer
            serializer to present and manipulate the data

        Methods
        -------
            search_image
                search for a specific image by tag or name within the images    
    '''
    queryset = models_gallery.Image.objects.all()
    serializer_class = serializer_gallery.ImageSerializer

    @action(detail=False, methods=['GET'], name='search_image')
    def search_image(self,request, pk=None):
        # http://127.0.0.1:8000/gallery/images/search_image/?value=Campo&albumid=1
        value = request.query_params.get('value')
        albumid = request.query_params.get('albumid')
        if value:
            image_search =models_gallery.Image.objects.filter(Q(name=value.rstrip()) | Q(tag=value.rstrip()),album=albumid)
            serializer = self.serializer_class(image_search, many=True)
            response = TemplateResponse(
                                status=status.HTTP_200_OK,error=False,
                                message="Resultado de Imagenes",body=serializer.data)
            return Response(response.getResponse())
        
        response = TemplateResponse(
                                status=status.HTTP_400_BAD_REQUEST,error=True,
                                message="No se especifico el tag o nombre",body=[])

        return Response(response.getResponse())





class GalleryViewSet(viewsets.ModelViewSet):
    queryset = models_gallery.get_user_model().objects.all()
    serializer_class = serializer_gallery.UsersGallery

    @action(detail=False, methods=['GET'], name='get_All_Albums')
    def get_All_Albums(self,request, pk=None):
        value = request.query_params.get('id')
        users = models_gallery.get_user_model().objects.get(id=value.rstrip())
        serializer = self.serializer_class(users, many=False)
        response = TemplateResponse(
                                status=status.HTTP_200_OK,error=False,
                                message="Result",body=serializer.data)
        return Response(response.getResponse())




class UserAuthToken(ObtainAuthToken):

    def getResponseTemplate(self,authentication,message,data):
        ''' Clase Plantilla'''
        return({
            'authentication': authentication,
            'message':message,
            'data': data
        })


    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if not serializer.is_valid():
            return Response(self.getResponseTemplate(False,"Invalid Credentials",None))
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(self.getResponseTemplate(True,"Authentication Succesful",{
            'token': token.key,
            'email': user.email,
            'name': user.name,
            'id':str(user.id)
        }))