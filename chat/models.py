from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_name = models.CharField(
        max_length=122,
        verbose_name='Фамилия',
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=122,
        verbose_name='Имя',
        blank=True,
        null=True
    )
    age = models.DateField(
        blank=True,
        null=True,
        verbose_name='Возраст'
    )
    image = models.ImageField(
        upload_to='images/avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    status = models.CharField(
        max_length=255,
        blank=True,
        default='.',
        verbose_name='Описание'
    )
    friends = models.ManyToManyField(
        'User',
        verbose_name='Друзья',
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Applicationfr(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='from_user'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )

    class Meta:
        verbose_name = 'Заявка на дружбу'
        verbose_name_plural = 'Заявки на дружбу'
        ordering = ['-date']


class Chat(models.Model):
    users = models.ManyToManyField(
        User,
        related_name='participants',
        verbose_name='Участники'
    )
    title = models.CharField(
        max_length=123,
        verbose_name='Название'
    )
    description = models.TextField(
        default='.',
        blank=True
    )
    avatar = models.ImageField(
        upload_to='images/avatars/%Y/%m/%d/',
        verbose_name='Изображение'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.TextField(
        verbose_name='Сообщение'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщении'


class ChatImage(models.Model):
    image = models.ImageField(
        upload_to='images/chat/images/%Y/%m/%d/',
        verbose_name='Изображение'
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )

    class Meta:
        verbose_name = 'Отзыв звонка'
        verbose_name_plural = 'Отзывы звонков'
        ordering = ['-date']


class ChatFile(models.Model):
    file = models.FileField(
        upload_to='files/chat/files/%Y/%m/%d/',
        verbose_name='Изображение'
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )

    class Meta:
        verbose_name = 'Файл чата'
        verbose_name_plural = 'Файлы чата'
        ordering = ['-date']


class Feedback(models.Model):
    content = models.TextField(
        verbose_name='Сообщение'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date']


RATE = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class FeedbackCall(models.Model):
    rate = models.CharField(
        max_length=10,
        choices=RATE,
    )
    context = models.TextField(
        verbose_name='Сообщение',
        blank=True,
        default='.'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление'
    )

    class Meta:
        verbose_name = 'Отзыв звонка'
        verbose_name_plural = 'Отзывы звонков'
        ordering = ['-date']
