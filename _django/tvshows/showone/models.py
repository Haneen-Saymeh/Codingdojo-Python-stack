from django.db import models

from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        
        return errors

    # def basic_validator2(self, postData):
    #     errorsedit = {}
    #     if len(postData['title2']) < 5:
    #         errorsedit["title2"] = "Show title should be at least 2 characters"
    #     if len(postData['network']) < 3:
    #         errorsedit["network"] = "Show network should be at least 3 characters"
    #     if len(postData['desc']) < 10:
    #         errorsedit["desc"] = "Show description should be at least 10 characters"
    #     return errorsedit


    
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


