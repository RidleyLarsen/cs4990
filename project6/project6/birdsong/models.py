from django.db import models
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from project6.accounts.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=139)

    class Meta:
        app_label = "birdsong"

    def __unicode__(self):
        return self.name


class Note(models.Model):
    reply_to = models.ForeignKey('Note', null=True, blank=True)
    profile = models.ForeignKey(Profile)
    mention = models.ForeignKey(Profile, null=True, blank=True, related_name="mention")
    text = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        app_label = "birdsong"
        ordering = ("-timestamp", )

    def __unicode__(self):
        return self.text

    @property
    def linked_text(self):
        tokens = self.text.split(' ')
        for i in range(len(tokens)):
            if tokens[i][0] == '#' and tokens[i].count('#') == 1 and tokens[i][1:].isalnum():
                tokens[i] = '<a href="{0}">{1}</a>'.format(
                    reverse('note-by-tag', args=(tokens[i][1:], )),
                    tokens[i]
                )
            elif tokens[i][0] == '@':
                counter = 1
                for c in range(1, len(tokens[i])):
                    counter = c
                    if not tokens[i][c].isalnum():
                        counter -= 1
                        break
                mention_name = tokens[i][1:counter + 1]
                try:
                    url = reverse('profiles:detail', args=(Profile.objects.get(user__username=mention_name).pk, ))
                    tokens[i] = '<a href="{0}">{1}</a>'.format(
                        url,
                        tokens[i]
                    )
                except:
                    pass
        return mark_safe(' '.join(tokens))
