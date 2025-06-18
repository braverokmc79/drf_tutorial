# from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         for field in ['title','code','linenos','language','style']:
#             setattr(instance, field, validated_data.get(field, getattr(instance, field)))
#         instance.save()
#         return instance

from importlib.metadata import requires
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	# ... 기존 필드 생략 ...
    owner = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.ReadOnlyField() # 두개 필드추가
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')       
    sampleTest = serializers.CharField(default="샘플 테스트 글자") #
    
    # owner, highlighted두개 필드 추가
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 
                  'linenos', 'language', 'style','owner',
                  'highlighted','highlight' ,"sampleTest"] 



# owner 사용자 API뷰 추가
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
            many=True, 
            queryset=Snippet.objects.all(),
            view_name='snippet-detail',
            required=False)
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets', 'password']



