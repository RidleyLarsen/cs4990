from django.db.models.signals import pre_save, post_save
from .models import Note, Profile, Tag


def set_tags(sender, instance, **kwargs):
    tokens = instance.text.split(' ')
    tagnames = []
    for token in tokens:
        if token[0] == '#' and token.count('#') == 1:
            tagname = ""
            for c in token[1:]:
                if c.isalnum():
                    tagname += c
                else:
                    break
            if len(tagname) > 0:
                tagnames.append(tagname)
            print tagname
    for name in tagnames:
        instance.tags.add(Tag.objects.get_or_create(name=name)[0])


def set_mention(sender, instance, **kwargs):
    tokens = instance.text.split(' ')
    if tokens[0][0] == "@":
        counter = 0
        for c in range(len(tokens[0][1:])):
            counter = c
            if not tokens[0][c + 1].isalnum():
                break
        mention_name = tokens[0][1:counter + 1]
        print mention_name
        try:
            profile = Profile.objects.get(user__username=mention_name)
        except Profile.DoesNotExist:
            profile = None
    else:
        profile = None
    instance.mention = profile

pre_save.connect(set_mention, sender=Note)
post_save.connect(set_tags, sender=Note)
