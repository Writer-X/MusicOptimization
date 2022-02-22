from django.contrib import admin

from .models import song_information
from .models import song_lyrics
from .models import software
from .models import user
from .models import musician
from .models import software_man
from .models import STOP

admin.site.register(song_information)
admin.site.register(song_lyrics)
admin.site.register(software)
admin.site.register(user)
admin.site.register(musician)
admin.site.register(software_man)
admin.site.register(STOP)