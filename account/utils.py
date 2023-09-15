import requests
import six
import os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.conf import settings

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()



def download_image(url):

    response = requests.get(url)
    print(settings.MEDIA_ROOT)
    file_name = 'profile_images/'  + url.split('/')[-1]  + '.png'
    file_path = os.path.join(settings.MEDIA_ROOT , file_name)
    print(file_path)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_name


