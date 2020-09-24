import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class VuePy(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        region = os.environ['DYNAMODB_REGION']
        host = os.environ['DYNAMODB_ENDPOINT']

    id = UnicodeAttribute(hash_key=True)

    countries = UnicodeAttribute(null=True)
