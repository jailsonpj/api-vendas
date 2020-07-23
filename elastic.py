from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan


user = "elastic"
passwd = "YgcFDLqEuhvxafts9Ulv8KHJ"
es = Elasticsearch(["https://elastic:YgcFDLqEuhvxafts9Ulv8KHJ@c01160965fdb47918c3d06933a6df089.us-east-1.aws.found.io:9243"])

index = "vendas-analysis"


def get_all():
    data = []

    match_all = {
        "query":{
            "match_all":{}
        }
    }
    resp = scan(es, index=index,query=match_all)
    for item in resp:
        data.append(item['_source'])

    return data

def get_material(material):
    data = []

    match = {
        "query":{
            "match":{
                "Material": material
            }
        }
    }

    resp = scan(es, index=index,query=match)
    for item in resp:
        #print(item['_source'])
        data.append(item['_source'])

    return data

def get_escrv(escrv):
    data = []

    match = {
        "query":{
            "match":{
                "Escrv": escrv
            }
        }
    }

    resp = scan(es, index=index,query=match)
    for item in resp:
        #print(item['_source'])
        data.append(item['_source'])

    return data

def get_data(data):
    data = []

    match = {
        "query":{
            "match":{
                "Data": data
            }
        }
    }

    resp = scan(es, index=index,query=match)
    for item in resp:
        #print(item['_source'])
        data.append(item['_source'])

    return data

def get_grp_merc(grpmerc):
    data = []

    match = {
        "query":{
            "match":{
                "GrpMerc": data
            }
        }
    }

    resp = scan(es, index=index,query=match)
    for item in resp:
        #print(item['_source'])
        data.append(item['_source'])

    return data