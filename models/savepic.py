#!/usr/bin/python
# -*- coding: utf-8 -*

from uuid import uuid4
from io import BytesIO
from PIL import Image


class SavePicture:
    def __init__(self,pic):
        self.thumb_size = (200, 200)
        self.savedir = "statics"
        self.imgdir = "imgs"
        self.thumbdir = 'thumbs'
        self.pic = pic
        self.uuid_name = self.get_uuidname()

    def get_uuidname(self):
        return uuid4().hex + "." + self.pic['filename'].split(".")[-1]

    def save_image(self):
        img_url = self.imgdir + "/" + self.uuid_name
        with open(self.savedir + "/" + img_url, "wb") as f:
            f.write(self.pic['body'])
        return img_url

    def save_thumb(self):
        thumb_url = self.thumbdir + '/{}x{}_{}'.format(self.thumb_size[0], self.thumb_size[1], self.uuid_name)
        bf = BytesIO()
        bf.write(self.pic['body'])
        im = Image.open(bf)
        im.thumbnail(self.thumb_size)
        im.save(self.savedir + '/' + thumb_url, "PNG")
        return thumb_url
