#Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model


class UserProfileManager(BaseUserManager):
    """
        base class for customize User functionalities
        ....

        Methods
        -------
        createUser(self,email,username,name,surname,password=None)
            Prepare the user by validating their data and then create it

        create_user(self,name,surname,email,username,password)
            Create the user and not provide superuser permissions    

        create_superuser(self,name,surname,email,username,password)
            Create te superuser and provide superuser permissions

    """
    def createUser(self,email,username,name,surname,password=None):
        '''
            Parameters
            ----------
            email: str
            username: str
            name: str
            surname: str
            password: str
        '''
        if not email:
            raise ValueError('Usuario debe tener un email')
        if not username:
            raise ValueError('Usuario debe tener un username')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,name=name,surname=surname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,name,surname,email,username,password):
        '''
            Parameters
            ----------
            email: str
            username: str
            name: str
            surname: str
            password: str
        '''
        user = self.createUser(email,username,name,surname,password)
        '''
            Parameters
            ----------
            email: str
            username: str
            name: str
            surname: str
            password: str
        '''
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self,name,surname,email,username,password):
        user = self.createUser(email,username,name,surname,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user







class UserProfile(AbstractBaseUser,PermissionsMixin):
    ''' 
        class to wrap custom django user
        ...

        Attributes:
        email: EmailField
            unique user email
        username: CharField
            unique username
        name: CharField
            personal name of the user 
        surname: CharField
            personal surname of the user
        is_active: BooleanField
            attribute that checks if it is unsubscribed
        is_staff: BooleanField
            attribute that checks the role of the django profile
        objects: UserProfileManager
            base class profile django
        USERNAME_FIELD: []
            configuration to customize the attribute to use for authentication
        REQUIRED_FIELDS: []
            configuration to customize mandatory attributes

        Methods
        -------
        get_fullname(self)
            Returns the full name of the user

        __str__(self)
            String Related

    '''
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=55,unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username','name','surname']

    def get_fullname(self):
        return '%s %s'%(self.name,self.surname)
    
    def __str__(self):
        return self.name




class Album(models.Model):
    """ 
        A class used to represent an Album model for to ORM 
        ...

        Attributes
        ----------
        album_name : CharField
            the name of the album
        create_at: DateField
            image creation date
        update_at: DateField
            image last update date
        user : User
            Nested relationship of the album to which the user belongs or
            Serializer relation, specifies to which user it belongs

        Methods
        -------   
        __str__(self)
            String Related #tag: album_name  

        Nested Classes
        --------------
            Meta:
                class Meta to customize Album Model default  
    """
    album_name = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now = True)
    user = models.ForeignKey(get_user_model(), 
                    related_name='gallery', on_delete=models.CASCADE)

    class Meta:
        """
            Attributes
            ----------
            ordering: []
                for ordering data with date creation    
        """
        ordering = ['create_at']

    def __str__(self):
        """ Specified string to identify the Album """
        return '%s' % (self.album_name)  




class Image(models.Model): 
    """
        A class used to represent an image model for to ORM
        ...       

        Attributes
        ----------
        name : CharField
            the name of the image
        tag : CharField
            search keyword
        link: CharField
            image access link
        create_at: DateField
            image creation date
        update_at: DateField
            image last update date
        album : Album
            Nested relationship of the album to which the image belongs

        Methods
        -------   
        __str__(self)
            String Related #tag: album_name  

        Nested Classes
        --------------
            Meta:
                class Meta to customize image Model default
    """
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now = True)
    album = models.ForeignKey(Album, 
                    related_name='images', on_delete=models.CASCADE)

    class Meta:
        """
            Attributes
            ----------
            ordering: []
                for ordering data with date creation    
        """
        ordering = ['create_at']

    def __str__(self):
        """ Specified string to identify the image """
        return '#%s: %s' % (self.tag, self.name)


