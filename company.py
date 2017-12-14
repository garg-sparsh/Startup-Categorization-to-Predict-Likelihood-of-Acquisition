import pickle,os
import json , csv
import pandas as pd
import numpy as np
pathp = 'company.csv'

class EntityParser:
    @staticmethod
    def LoadJsonEntity(filename):
        text = EntityParser.LoadStringEntityByFilename(filename)
        js = None
        try:
            if text:
                js = json.loads(text)
        except ValueError as e:
            print(e)
        return js

    @staticmethod
    def LoadStringEntityByFileHandler(fid):
        if fid:
            return pickle.load(fid)
        else:
            return ''

    @staticmethod
    def LoadStringEntityByFilename(filename, mode='rb'):
        try:
            fid = open(filename, mode)
        except IOError:
            fid = None
        obj = None
        if fid:
            try:
                obj = pickle.load(fid)
            except ValueError as e:
                obj = None
        return obj


def main():
    with open(pathp, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['name',
                'permalink',
                'crunchbase_url',
                'homepage_url',
                'blog_url',
                'blog_feed_url',
                'twitter_username',
                'category_code',
                'number_of_employees',
                'founded_year',
                'founded_month',
                'founded_day',
                'deadpooled_year',
                'deadpooled_month',
                'deadpooled_day',
                'deadpooled_url',
                'tag_list',
                'alias_list',
                'email_address',
                'phone_number',
                'description',
                'created_at',
                'updated_at',
                'overview',
                'image',
                'products',
                'relationships',
                'competitions',
                'providerships',
                'total_money_raised',
                'funding_rounds',
                'investments',
                'acquisition',
                'acquisitions',
                'offices',
                'milestones',
                'ipo',
                'video_embeds',
                'screenshots',
                'external_links'])

    dir = '/home/sgarg/P3/company'
    for personFiles in os.listdir(dir):
        path = dir+personFiles
        js = EntityParser.LoadJsonEntity(path)
        if js:
            colX=['name',
                'permalink',
                'crunchbase_url',
                'homepage_url',
                'blog_url',
                'blog_feed_url',
                'twitter_username',
                'category_code',
                'number_of_employees',
                'founded_year',
                'founded_month',
                'founded_day',
                'deadpooled_year',
                'deadpooled_month',
                'deadpooled_day',
                'deadpooled_url',
                'tag_list',
                'alias_list',
                'email_address',
                'phone_number',
                'description',
                'created_at',
                'updated_at',
                'overview',
                'image',
                'products',
                'relationships',
                'competitions',
                'providerships',
                'total_money_raised',
                'funding_rounds',
                'investments',
                'acquisition',
                'acquisitions',
                'offices',
                'milestones',
                'ipo',
                'video_embeds',
                'screenshots',
                'external_links']
            df = pd.columns=colX
            index=0
            my_array=[]
            for da in js.items():
                df[index]=da[1]
                my_array.append(da[1])
                index=index+1

        else:
            print("no json object")
        with open(pathp, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(colX)


if __name__ == "__main__":
    main()
