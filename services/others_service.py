from cloudinary import uploader

def upload_post_to_cloudinary(cover):
    response =  uploader.upload(cover, folder='posts')
    return response.get('secure_url')

def upload_photo_to_cloudinary(photo):
    response = uploader.upload(photo, folder='photos')
    return response.get('secure_url')