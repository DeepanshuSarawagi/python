from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    """
        In this model class, we are going to establish a ont-to-one relationship with Address and Author.
        Which is one address for one author. We can create a relationship by using a one-to-one field.
        Remember that, we wont use the ForeignKey field since that is used for the many-to-one relationship.
        In one-to-one relationship we dont have to specify the related_name as an argument in the OneToOneField.
    """
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=7)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

    class Meta:
        verbose_name_plural = "Address Entries"  # This is being done to fix the plural form of Address model in the
        # django admin site. Django allows us to create the Meta inner-class for the models which will allow us to
        # change the behaviour of fields/attributes


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()


class Book(models.Model):

    title = models.CharField(max_length=100)  # CharField() is a Django Model field type. This shows what kind of
    # data we will store in title field
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # IntegerField() is a Django Model field type. This shows what kind of
    # data we will store in title field. We have added the validators as a Keyword arg by importing
    # the validators class and instantiating the Min and MaxValueValidator
    # author = models.CharField(null=True, max_length=100)
    # Above code is commented because we are creating a separate class for Author to build a one-to-many relationship
    # between and author and their books. Hence we will set the author field to a Foreign Key field and it will accept
    # one argument which is a model i.e., to which model we can build the relationship with
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")  # We have now set the relationship
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
    published_countries = models.ManyToManyField(Country)  # We are now establishing a ManyToMany relationship between
    # Book and Country model. In this case, we need not specify the on_delete=models.CASCADE because deleting a book
    # in a country should not delete the book object itself. This relationship is setup differently. Most relationship
    # are created with two tables. But in this case, there is a third table created. it is mapping table
    # between book and country. If a book belongs to two countries, then two rows will be created between this mapping
    # table. Therefore, when we delete a country, Book model will not be affected at all.

    """
    Book -> Primary model
    Book.author is the field
    Author -> related model
    
        After establishing relationship between Book and Author model, we can also use query sets to query the related
        data of which relationship is established.
        For example, we can find all the books by an author whose last_name is Rowling. The django query would be
        Book.objects.filter(author__last_name="Rowling")  -> Here author is the field of Book class and since we have
        established a relationship on Author model, we can get the Author's last name. So author is the field of Book
        model and last_name is the field of Author model.
        
        We can also use the modifiers in the query.
        for example:
        => rowling_books = Book.objects.filter(author__last_name__contains="wling")
        This will return us the QuerySet of books by author whose last name contains wling -> Ro'wling'
        
        We can also query the Author and all the books by the author. Since we do not have any book field in the Author 
        class, Django automatically creates a book_set since it has a relationship with the Book class
        Refer to the below query.
        => jkr = Author.objects.get(first_name="J.K.")
        => jkr.book_set.all()
        This above query will return all the books by Author whose first_name is J.K.
        Note: Django automatically creates the book_set property on the Author object. It takes the class name of the 
        model and creates a set of related data.
        The alternate method to get all the books by an author is to set the value of one more named parameter called 
        "related_name". We need to pass this named argument in the field where we have established relationship with the
        remote model. In our case it will be the "author" ForeignKey field of Book class. For e.g.
        author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
        Now we can query the books by an author like this
        => jkr.books.all()
        
        Once we have got the Query set of books, we can now apply filters to query a certain set of data using the 
        modifiers. For example, we can filter all the books by an author whose rating is greater than 3
        => jkr.books.filter(rating__gt=3)
    """

    """
    Book -> Primary model
    Book.published_countries is the field
    Country -> Related model
    
    We are now going to form a ManyToMany relationship between Book and Country. Which means a book can be published in 
    many countries and a country can have many books.
    We created the Book.country field of type ManyToMany(Country).
    In this case, we need not specify the on_delete=models.CASCADE because deleting a book
    # in a country should not delete the book object itself. This relationship is setup differently. Most relationship
    # are created with two tables. But in this case, there is a third table created. it is mapping table
    # between book and country. If a book belongs to two countries, then two rows will be created between this mapping
    # table. Therefore, when we delete a country, Book model will not be affected at all.
    
    We first create Book objects and Country objects and then using the book object, we assign the values to the 
    Book.published_countries using the following method. For example,
    => india = Country(name="India", code="IN")
    => meluha = Book.objects.get(title="Immortals of Meluha")
    => meluha.published_countries.add(india)
    
    Note that, we need to call the .add() method on the published_countries field. Since it is a 
    ManyToMany relationship field, Django automatically creates this method.
    
    To retrieve books published in a country, we just need to use the following method
    => india = Country.objects.get(code="IN")
    => india.book_set.all()
    This will return the QuerySet of all the books published in India  
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
