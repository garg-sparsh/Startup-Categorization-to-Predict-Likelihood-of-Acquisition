import pickle,os
import json , csv
import pandas as pd
import numpy as np
pathp = '/Users/prakharmaheshwari/Desktop/product.csv'

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
        writer.writerow(['name',
                    'permalink',
                    'crunchbase_url',
                    'homepage_url',
                    'blog_url',
                    'blog_feed_url',
                    'twitter_username',
                    'stage_code',
                    'deadpooled_url',
                    'invite_share_url',
                    'tag_list',
                    'alias_list',
                    'deadpooled_year',
                    'deadpooled_month',
                    'deadpooled_day',
                    'launched_year',
                    'launched_month',
                    'launched_day',
                    'created_at',
                    'updated_at',
                    'overview',
                    'image',
                    'company',
                    'milestones',
                    'video_embeds',
                    'external_links'])

    dir = '/Users/prakharmaheshwari/Downloads/product/'
    # for pers
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
                    'stage_code',
                    'deadpooled_url',
                    'invite_share_url',
                    'tag_list',
                    'alias_list',
                    'deadpooled_year',
                    'deadpooled_month',
                    'deadpooled_day',
                    'launched_year',
                    'launched_month',
                    'launched_day',
                    'created_at',
                    'updated_at',
                    'overview',
                    'image',
                    'company',
                    'milestones',
                    'video_embeds',
                    'external_links']
            df = pd.columns=colX
            # for i, item in enumerate(js):
                # print(""+str(i)+"============="+item)
                # print(item)
                # for key in item.keys():
                #     print(key, "=", item[key])
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