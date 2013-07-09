from django.db import models


class Log(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        username = self.user.username
        text = self.text[:20] + '...' if len(self.text) > 20 else self.text
        date = self.date.strftime('%d/%m/%Y %H:%M')

        return '{0} - {1}: {2}'.format(date, username, text)
