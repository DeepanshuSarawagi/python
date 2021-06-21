from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):

    title = models.CharField(max_length=100)  # CharField() is a Django Model field type. This shows what kind of
    # data we will store in title field
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # IntegerField() is a Django Model field type. This shows what kind of
    # data we will store in title field. We have added the validators as a Keyword arg by importing
    # the validators class and instantiating the Min and MaxValueValidator
    # author = models.CharField(null=True, max_length=100)
    # Above code is commented because we are creating a separate class for Author to build a one-to-many relationship
    # between and author and their books. Hence we will set the author field to a Foreign Key field and it will accept
    # one argument which is a model i.e., to which model we can build the relationship with
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)  # We have now set the relationship
    # between book and the author. We now need to let the model know that what happens if the object with which we
    # are building relationship gets deleted. In that case, we need to use the on_delete=CASCADE which means,
    # delete all the related model objects before deleting the remote model object
    is_bestselling = models.BooleanField(default=False)
    # slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # Harry Potter 1 => harry-potter-1
    # We have used db_index=True which will create a index for this field in the table since we use it a lot,
    # which will improve the performance of find operation whenever an Object is looked up using this field
    # Setting blank=True so that it is not a required field in the django admin site
    # Setting the field Editable=False so that it doesnt show up in admin site
    """
        After establishing relationship between Book and Author model, we can also use query sets to query the related
        data of which relationship is established.
        For example, we can find all the books by an author whose last_name is Rowling. The django query would be
        Book.objects.filter(author__last_name="Rowling")  -> Here author is the field of Book class and since we have
        established a relationship on Author model, we can get the Author's last name. So author is the field of Book
        model and last_name is the field of Author model.
    """

    def get_absolute_url(self):  # We are overriding this method which automatically gets called by Django to load
        # the specific url/page
        return reverse("book-detail", args=[self.slug])

    # Here we are overwriting the save() method and slugifying the title of the book
    # This slugified field will be then used in the URLs
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Book, self).save()

    def __str__(self):
        return f"{self.title} {self.rating}"
