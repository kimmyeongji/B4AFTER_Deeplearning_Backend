from rest_framework import serializers
from post.models import Post, Image, Comment, ImageModel

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    class Meta:
        model = Image
        fields = '__all__'

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('before_image', 'model', 'after_image',)
        
class ImageModelSerializer(serializers.ModelSerializer):
    model = serializers.SerializerMethodField()
    
    def get_model(self,obj):
        return obj.model.name
    class Meta:
        model = ImageModel
        fields = ('model',)

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    image = ImageSerializer()
    likes = serializers.StringRelatedField(many=True)
    like_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        return obj.image

    def get_like_count(self, obj):
        return obj.likes.count()
    class Meta:
        model = Post
        fields = ('id', 'user', 'image', 'update_at', 'likes', 'like_count')

class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    image = ImageSerializer()
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()
    likes = serializers.StringRelatedField(many=True)
    like_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        return obj.image

    def get_comments(self, obj):
        return obj.comments
    
    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_likes(self, obj):
        return obj.likes.user.username

    def get_like_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
        
    class Meta:
        model = Post
        fields = ('user','image', 'content')

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content',)