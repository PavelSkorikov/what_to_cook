from django.db import models
import uuid
# импортируем стандартную Django - модель пользователя
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingridient(models.Model):
    # Модель ингридинета
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Нименование", max_length=256, blank=False)

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
    def __str__(self):
        return self.name


class Steps(models.Model):
    # Шаги приготовления рецепта
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField("Номер этапа", blank=False, default=0)
    image = models.ImageField("Изображение", upload_to='uploads/steps/%Y/%m/%d/', height_field=None, width_field=None,
                              max_length=100)
    action = models.TextField("Действие", max_length=3024, default=None)

    class Meta:
        verbose_name = "Этап приготовления"
        verbose_name_plural = "Этапы приготовления"
    def __str__(self):
        num = str(self.number)
        return num


class Recipe(models.Model):
    # Модель рецепта
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Название", max_length=256, unique=True)
    DISH_NAME = (
        ('FIRST', 'ПЕРВОЕ'),
        ('SECOND', 'ВТОРОЕ'),
        ('DESSERT', 'ДЕСЕРТ'),
        ('SNACK', 'ЗАКУСКА'),
        ('FASTFOOD', 'ПЕРЕКУСИТЬ ПО БЫСТРОМУ'),
        ('DRINK', 'НАПИТКИ')
    )
    dish = models.CharField("Блюдо", max_length=10, choices=DISH_NAME, default='NO' )
    description = models.TextField("Описание", max_length=5000, blank=True)
    ingredients = models.TextField("Ингредиенты", max_length=5000, default=None, null=True)
    procedure = models.TextField("Порядок приготовления", max_length=5000, default=None)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    image = models.ImageField("Изображение", upload_to='uploads/%Y/%m/%d/', height_field=None, width_field=None,
                              max_length=100)
    cooking_time = models.CharField("Время приготовления", max_length=50, default='0 мин', blank=True)
    servings = models.IntegerField("Количество порций", default=1, blank=True)
    likes = models.IntegerField("Лайки", default=0, blank=True)
    dislikes = models.IntegerField("Дизлайки", default=0, blank=True)
    COMPLEXITY = (
        ('EASY', 'Простой'),
        ('MIDLE', 'Средний'),
        ('HARD', 'Сложный'),
        ('SUPER_HARD', 'Очень сложный'),
    )
    complexity = models.CharField("Сложность приготовления", max_length=50, choices=COMPLEXITY, default='Простой', blank=True)
    steps = models.ForeignKey(Steps, verbose_name='этапы пригтовления', null=True, blank=True, on_delete=models.SET_NULL)
    # дата создания записи в базе
    createAt = models.DateField("Дата создания", auto_now_add=True)
    # связанная модель пользователя, который оставил рецепт
    user = models.ForeignKey(User, verbose_name='автор', on_delete=models.SET('remoted_user'))

    class Meta:
        ordering = ['createAt']
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title

class Comments(models.Model):
    # комментарии к рецепту
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField("Комментарий к рецепту", max_length=5000, default=None)
    user = models.ForeignKey(User, verbose_name='автор комментария', on_delete=models.SET('anonimous_user'))
    recipe = models.ForeignKey(Recipe, verbose_name='рецепт', on_delete=models.CASCADE)
    createAt = models.DateField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ['createAt']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комменетарии"

    def __str__(self):
        return self.recipe
