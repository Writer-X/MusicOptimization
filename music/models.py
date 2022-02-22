from django.db import models

class song_information(models.Model):
    song_ID = models.IntegerField(primary_key=True, db_index=True)
    song_name = models.CharField(max_length=10)
    singer = models.CharField(max_length=4)
    lyrics_maker = models.CharField(max_length=4)
    composer = models.CharField(max_length=4)
    time = models.CharField(max_length=6)
    software = models.CharField(max_length=10)
    need_VIP = models.CharField(max_length=3)
    need_pay = models.CharField(max_length=3)
    payment = models.IntegerField()
    tone_quality = models.CharField(max_length=10)
    interlinkage = models.CharField(max_length=200)
    click_number = models.IntegerField()
    search_number = models.IntegerField()

    def __str__(self):
        return self.song_name

class song_lyrics(models.Model):
    song_ID = models.IntegerField(primary_key=True, db_index=True)
    lyrics = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.song_ID)

class user(models.Model):
    user_ID = models.IntegerField(primary_key=True, db_index=True)
    user_account = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_introduction = models.CharField(max_length=50, null=True)
    user_email = models.CharField(max_length=20)
    user_verification = models.CharField(max_length=4, null=True)
    def __str__(self):
        return self.user_account

class software(models.Model):
    software_ID = models.IntegerField(primary_key=True)
    software_name = models.CharField(max_length=10)
    song_numbers = models.IntegerField()
    pay_of_VIP = models.CharField(max_length=10)
    click_number = models.IntegerField()
    def __str__(self):
        return self.software_name

class musician(models.Model):
    musician_ID = models.IntegerField(primary_key=True, db_index=True)
    musician_name = models.CharField(max_length=10)
    musician_sex = models.CharField(max_length=1)
    musician_age = models.IntegerField()
    musician_kind = models.CharField(max_length=3)
    click_number = models.IntegerField()
    def __str__(self):
        return self.musician_name

class software_man(models.Model):
    software_man_ID = models.IntegerField(primary_key=True, db_index=True)
    software_man_account = models.CharField(max_length=20)
    software_man_password = models.CharField(max_length=20)
    software_man_name = models.CharField(max_length=10)
    software_man_sex = models.CharField(max_length=1)
    software_man_age = models.IntegerField()
    software_man_phone = models.CharField(max_length=11)
    software_man_email = models.CharField(max_length=20)
    software_ID =models.ForeignKey('software', on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return self.software_man_name


class manager(models.Model):
    manager_ID = models.IntegerField(primary_key=True, db_index=True)
    manager_account = models.CharField(max_length=20)
    manager_password = models.CharField(max_length=20)
    manager_name = models.CharField(max_length=10)
    manager_sex = models.CharField(max_length=1)
    manager_age = models.IntegerField()
    manager_phone = models.CharField(max_length=11)
    manager_email = models.CharField(max_length=20)

    def __str__(self):
        return self.manager_name

class STOP(models.Model):
    song_number = models.IntegerField(primary_key=True, db_index=True)
    song_name = models.CharField(max_length=10)
    search_number = models.IntegerField()

    def __str__(self):
        return str(self.song_number)

class CTOP(models.Model):
    ranking = models.IntegerField(primary_key=True)
    song_ID = models.ForeignKey('song_information', on_delete=models.CASCADE)
    song_name = models.CharField(max_length=10)
    click_number = models.IntegerField()

    def __str__(self):
        return str(self.ranking)

class Best_singer(models.Model):
    ranking = models.IntegerField(primary_key=True)
    musician_ID = models.ForeignKey('musician', on_delete=models.CASCADE)
    musician_name = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    click_number = models.IntegerField()

    def __str__(self):
        return str(self.ranking)

class Best_software(models.Model):
    ranking = models.IntegerField(primary_key=True)
    software_ID = models.ForeignKey('software', on_delete=models.CASCADE)
    software_name = models.CharField(max_length=10)
    song_number = models.IntegerField()
    pay_of_VIP = models.CharField(max_length=10)
    click_number = models.IntegerField()

    def __str__(self):
        return str(self.ranking)

class Best_lyrics_maker(models.Model):
    ranking = models.IntegerField(primary_key=True)
    musician_ID = models.ForeignKey('musician', on_delete=models.CASCADE)
    musician_name = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    click_number = models.IntegerField()

    def __str__(self):
        return str(self.ranking)

class Best_composer(models.Model):
    ranking = models.IntegerField(primary_key=True)
    musician_ID = models.ForeignKey('musician', on_delete=models.CASCADE)
    musician_name = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    click_number = models.IntegerField()

    def __str__(self):
        return str(self.ranking)


class collection(models.Model):
    collection_number = models.IntegerField(primary_key=True, db_index=True)
    song_ID = models.ForeignKey('song_information', on_delete=models.CASCADE, db_index=True)
    user_ID = models.ForeignKey('user', on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return self.collection_number

class Song_list(models.Model):
    songlist_number = models.IntegerField(primary_key=True, db_index=True)
    songlist_name = models.CharField(max_length=10)
    song_ID = models.ForeignKey('song_information', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.songlist_number)