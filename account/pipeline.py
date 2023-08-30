from account.utils import download_image

def get_user_image(backend, strategy, user, response, is_new=False,*args,**kwargs):
    if user.image:
        return None
    url = "https://img.freepik.com/premium-vector/account-icon-user-icon-vector-graphics_292645-552.jpg"
    if backend.name == "facebook":
        url = f"http://graph.facebook.com/{response['id']}/picture?type=large"
    elif backend.name == 'google-oauth2':
        url = response['picture']
    
    user.image = download_image(url)
    user.save()
    