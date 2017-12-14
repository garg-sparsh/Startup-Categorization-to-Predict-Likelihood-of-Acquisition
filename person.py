import pickle,os
import json , csv
import pandas as pd
import numpy as np
pathp = 'person.csv'

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
            print(fid)
            try:
                obj = pickle.load(fid)
            except ValueError as e:
                obj = None
        return obj

    # @staticmethod
    # def get_file_handler(filename, mode):
    #     try:
    #         fid = open(filename, mode)
    #     except IOError:
    #         fid = None
    #     return fid


def main():
    with open(pathp, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['first_name','last_name',
                                             'permalink',
                                             'crunchbase_url',
                                             'homepage_url',
                                             'birthplace',
                                             'twitter_username',
                                             'blog_url',
                                             'blog_feed_url',
                                             'affiliation_name',
                                             'born_year',
                                             'born_month',
                                             'born_day',
                                             'tag_list',
                                             'alias_list',
                                             'created_at',
                                             'updated_at',
                                             'overview',
                                             'image',
                                             'degrees',
                                             'relationships',
                                             'investments',
                                             'milestones',
                                             'video_embeds',
                                             'external_links',
                                             'web_presences'])

    dir = '/home/sgarg/P3/person'
    # for pers
    for personFiles in os.listdir(dir):
        path = '/home/sgarg/P3/person'+personFiles
        js = EntityParser.LoadJsonEntity(path)
        if js:
            colX=['first_name','last_name',
                                                 'permalink',
                                                 'crunchbase_url',
                                                 'homepage_url',
                                                 'birthplace',
                                                 'twitter_username',
                                                 'blog_url',
                                                 'blog_feed_url',
                                                 'affiliation_name',
                                                 'born_year',
                                                 'born_month',
                                                 'born_day',
                                                 'tag_list',
                                                 'alias_list',
                                                 'created_at',
                                                 'updated_at',
                                                 'overview',
                                                 'image',
                                                 'degrees',
                                                 'relationships',
                                                 'investments',
                                                 'milestones',
                                                 'video_embeds',
                                                 'external_links',
                                                 'web_presences']
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
