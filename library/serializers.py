from rest_framework import serializers
from .models import Author, Genre, Book, Loan
from users.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genre', write_only=True, allow_null=True)

    class Meta:
        model = Book
        fields = '__all__'

# class LoanSerializer(serializers.ModelSerializer):
#     book = BookSerializer(read_only=True)
#     user = serializers.StringRelatedField(read_only=True) # display username instead of pk
#     class Meta:
#         model = Loan
#         fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True)
    
    class Meta:
        model = Loan
        fields = ['id', 'book', 'book_id', 'user', 'user_id', 'loan_date', 'due_date', 'return_date']