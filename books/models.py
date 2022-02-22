from django.db import models

class Books(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    booklan = models.CharField(max_length=100, blank=True, default='')
    bookname = models.CharField(max_length=100, blank=True, default='')
    bookauthor = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        """ Use the `pygments` library to create a highlighted HTML
        representation of the code snips.
        """
        booklan = {'Book Language': self.booklan} if self.booklan else {}
        bookname = {'Book Name': self.bookname} if self.bookname else {}
        bookauthor = {'Book Author': self.bookauthor} if self.bookauthor else {}
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['created']
