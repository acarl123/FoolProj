from django.db import models

# Create your models here.


class Article(models.Model):
    disclosure = models.CharField(max_length=250, blank=True, null=True)
    promo = models.CharField(max_length=250, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    article_type = models.CharField(max_length=50, blank=True, null=True)
    publish_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    path = models.URLField(max_length=200, blank=True, null=True)
    static_page = models.BooleanField(blank=True, null=True)
    author_override = models.BooleanField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    headline = models.CharField(max_length=50, blank=True, null=True)
    modified = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    video = models.URLField(max_length=200, blank=True, null=True)
    byline = models.CharField(max_length=50, blank=True, null=True)

    instruments = models.ManyToManyField("Instrument")
    authors = models.ManyToManyField("Author")
    bureau = models.ForeignKey("Bureau", on_delete=models.CASCADE, blank=True, null=True)
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag")
    images = models.ManyToManyField("Image")
    pitch = models.ForeignKey("Pitch", on_delete=models.CASCADE, blank=True, null=True)
    links = models.ForeignKey("Links", on_delete=models.CASCADE, blank=True, null=True)

class Instrument(models.Model):
    instrument_id = models.IntegerField()
    asset_class = models.CharField(max_length=50)
    exchange = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    primary = models.BooleanField()
    seo_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    syndicate = models.BooleanField()
    valid = models.BooleanField()

    links = models.ForeignKey("Links", on_delete=models.CASCADE)


class Links(models.Model):
    content = models.URLField(max_length=200, blank=True, null=True)
    self = models.URLField(max_length=200, blank=True, null=True)
    presentation = models.URLField(max_length=200, blank=True, null=True)
    content_sequence = models.URLField(max_length=200, blank=True, null=True)


class Author(models.Model):
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fool_uid = models.IntegerField()
    primary = models.BooleanField()
    twitter_username = models.CharField(max_length=50, null=True, blank=True)
    small_avatar_url = models.URLField(max_length=200)
    long_bio = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=50)
    byline = models.CharField(max_length=50)
    uuid = models.CharField(max_length=50)
    contributor_type = models.CharField(max_length=50)
    large_avatar_url = models.URLField(max_length=200)
    short_bio = models.CharField(max_length=250)
    author_id = models.IntegerField()
    email = models.EmailField(max_length=254)

    links = models.ForeignKey("Links", on_delete=models.CASCADE)


class Bureau(models.Model):
    uuid = models.CharField(max_length=50)
    slug = models.SlugField()
    name = models.CharField(max_length=50)

    links = models.ForeignKey("Links", on_delete=models.CASCADE)


class Collection(models.Model):
    uuid = models.CharField(max_length=50)
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    path = models.URLField(max_length=200)

    links = models.ForeignKey("Links", on_delete=models.CASCADE)


class Tag(models.Model):
    uuid = models.CharField(max_length=50)
    slug = models.SlugField()
    name = models.CharField(max_length=50)

    tag_type = models.ForeignKey("Tag_type", on_delete=models.CASCADE)
    links = models.ForeignKey("Links", on_delete=models.CASCADE)


class Tag_type(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50)


class Image(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    url = models.URLField(max_length=200)
    image = models.URLField(max_length=200)
    modified = models.DateTimeField(auto_now=False, auto_now_add=False)
    featured = models.BooleanField()
    uuid = models.CharField(max_length=50)


class Pitch(models.Model):
    text = models.TextField()
    id = models.IntegerField(primary_key=True)


class Comment(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
