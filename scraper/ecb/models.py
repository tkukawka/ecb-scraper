from django.db import models


class RSSFeedModel(models.Model):
    target = models.CharField(max_length=5, blank=True, null=True)  # cb_targetcurrency
    date = models.DateTimeField(default=None, blank=True, null=True)  # updated_parsed
    link = models.URLField(default=None, blank=True, null=True)  # link
    exchange_rate = models.CharField(max_length=20, blank=True, null=True)  # cb_exchangerate
    title = models.CharField(max_length=100, blank=True, null=True)  #  title
    summary = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # primary keys chosen as a determinant for new data
        unique_together = (("target", "date"),)

    def __str__(self):
        return "{} - {}".format(self.target, self.date)
