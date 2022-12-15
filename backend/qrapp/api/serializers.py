
from rest_framework import serializers

from qrapp.models import BarCode
from rest_framework.validators import UniqueValidator
# ChartGroupListSerializer

class BarCodeListSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='name')
    # description = serializers.CharField('')
    class Meta:
        model = BarCode
        fields = [
            'id',
            'created_at',
            'printed_at',
            'status',
            'uid',
        ]
        
    uid = serializers.SerializerMethodField('get_uid')
    
    def get_uid(self, barCode :BarCode):
        return f"{barCode.id:016}"
    
        
class BarCodeCreateSerializer(serializers.ModelSerializer):
    # A field from the user's profile:
    # username = serializers.SlugField(
    #     min_length=4,
    #     max_length=32,
    #     help_text=
    #         'Required. 4-32 characters. Letters, numbers, underscores or hyphens only.'
    #     ,
    #     validators=[UniqueValidator(
    #         queryset=BarCode.objects.all(),
    #         message='has already been taken by other user'
    #     )],
    #     required=True
    # )
    # password = serializers.CharField(
    #     min_length=4,
    #     max_length=32,
    #     write_only=True,
    #     help_text=
    #         'Required. 4-32 characters.'
    #     ,
    #     required=True
    # )
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(
    #         queryset=User.objects.all(),
    #         message='has already been taken by other user'
    #     )]
    # )
    # bio = serializers.CharField(source='profile.bio', allow_blank=True, default='')
    # name = serializers.CharField(
    #     source='profile.name',
    #     allow_blank=True,
    #     default='',
    #     max_length=32
    # )
    # avatar = serializers.URLField(source='profile.avatar', allow_blank=True, default='')
    # status = serializers.CharField(
    # 	source='profile.status',
    # 	allow_blank=True,
    # 	max_length=16,
    #     min_length=0,
    #     default=''
    # )
    
    class Meta:
        model = BarCode
        fields = (
            'id',
            'printed_at',
            'created_at',
            'status',
        )
        
        # read_only_fields = ('uid',)