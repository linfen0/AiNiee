import json
import pandas as pd
import os
from tqdm import tqdm
import translate_through_llm as ttl
# 读取CSV文件


# 假设我们要修改第二行的第三列
# 使用.loc来定位并修改
# 
def translate_context_through_dict(context,dict,source_lang:str,target_lang:str,text_separators:list=['\n','${heart}'],use_llm=False):
    '''
    context: 要翻译的文本\n
    dict: 翻译字典\n
    source_lang: 源语言\n
    target_lang: 目标语言\n
    text_separators: 文本分隔符，默认为['\n','${heart}']\n
    use_llm: 当翻译失败时是否使用llm进行翻译，默认为False\n
    '''
    ans = ''
    if not isinstance(context,str):
        return context
    import re
    pattern='|'.join(re.escape(delimiter) for delimiter in text_separators)
    keys=re.split(f'({pattern})',context)
    for k in keys:
        if k in text_separators:
            ans+=k
        else:
            is_source_lang=False
            for c in k:
                if __get_Lang(c)==source_lang:
                    is_source_lang=True
                    break
            if is_source_lang:
                try:
                    temp=dict[k]
                    if temp.count('\\"')%2!=0:
                        temp=temp.replace('\\"','')
                except KeyError:
                    if not use_llm:
                        temp=k#如果翻译失败，将原文作为翻译结果 
                    else:
                        temp=ttl.translatllm(k)#模块原本是用来翻译整段的，所以需要index参数来决定究竟翻译那一段
                ans+=temp
            else:#非目标源语言，不需要翻译
                ans+=k
    if ans!='nan' and ans.count('Unnamed')==0:
        return f"{ans}"
    else:
        return ''
    
def __saveFile(df:pd.DataFrame, output_directory, override=False):
    dir = os.path.dirname(output_directory)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
    if override or (not override and not os.path.exists(output_directory)):
        df.to_csv(output_directory, index=False, encoding='utf-8')       

def __get_Lang(char):
        if '\u4e00' <= char <= '\u9fff':
            return 'zh-cn'
        if '\u0800' <= char <= '\u4e00':
            return 'ja'
        if '\u0000' <= char <= '\u0800':
            return 'en'
      
def translate_exported_csvfile_through_dict(exported_csv_path,translated_json_path,write_column_index,output_directory,override=True):
    '''这个函数会把由mtool导出的手动翻译文件，同步到Translator++导出的csv文件中，便于对接Translator++还不支持的翻译方式，例如chatGPT\n
    exported_csv_path: Translator++导出的csv文件路径\n
    translated_json_path: mtool导出的json翻译文件路径\n
    write_column_index: 要写入的列索引\n
    output_directory: 同步完成后的csv文件路径\n
    override: 是否覆盖原文件，默认为True\n
    
        '''
    df = pd.read_csv(exported_csv_path)
    with open(translated_json_path, 'r', encoding='utf-8') as f:
        mtool_trans = json.load(f)
        
    for row in range(len(df)):
        raw_key=df.loc[row, df.columns[0]]
        df.loc[row, df.columns[write_column_index]]=translate_context_through_dict(raw_key,mtool_trans,'ja','zh-cn')
        
    __saveFile(df, output_directory, override)
#
def translate_Database_through_dict(DataBase_File,translated_json_path,output_directory,override=True):
    '''
     
    '''
    if override and os.path.exists(output_directory):
        return
    try:
        df=pd.read_csv(DataBase_File,encoding='Shift-JIS')
    except:
        df=pd.read_csv(DataBase_File,encoding='utf-8')
        
    with open(translated_json_path, 'r', encoding='utf-8') as f:
        dic=json.load(f)
 
    for row in range(len(df)):
        for column_i in range(len(df.columns)):
                raw_key=df.loc[row, df.columns[column_i]]
                df.loc[row, df.columns[column_i]]=translate_context_through_dict(raw_key,dic,'ja','zh-cn')
    
    #一定要最后更改表头，否则无法找到目标列
    for column in df.columns:
        temp=translate_context_through_dict(column,dic,'ja','zh-cn')
        df.rename(columns={column:temp},inplace=True)
    __saveFile(df, output_directory, override)
    
def translatorPP_sync_Mtool():
    exported_csv_directory="TRANS"
    translated_json_path="双六翻译_本体_DLC.json" 
    output_directory="output_trans"
    for dir_path,_, files in os.walk(exported_csv_directory):
        for file in files:
            if file.endswith(".csv"):
                exported_csv_path=os.path.join(dir_path, file)
                output_csv_path=os.path.join(output_directory,dir_path,file)
                try:
                    translate_exported_csvfile_through_dict(exported_csv_path,translated_json_path,1,output_csv_path)
                except Exception as e:
                    print(f"Error: {e}")
                    continue

def __search_dict(obj,translated_dict:dict,source_lang,target_lang):
    if isinstance(obj,str):
        return translate_context_through_dict(obj,translated_dict,source_lang,target_lang,use_llm=True)
    if isinstance(obj,list):
        for i in range(len(obj)):
            obj[i]=__search_dict(obj[i],translated_dict,source_lang,target_lang)
    if isinstance(obj,dict):
        for key in obj.keys():
            if key=='list':
                pass
            obj[key]=__search_dict(obj[key],translated_dict,source_lang,target_lang)
    
    return obj
 
def translate_json_througn_dict(input_path,output_path,dict_path,source_lang,target_lang):
    with open(input_path, 'r', encoding='utf-8') as inf:
        dic=json.load(inf)
    with open(dict_path, 'r', encoding='utf-8') as tf:
        translated_dict=json.load(tf)
    __search_dict(dic,translated_dict,source_lang=source_lang,target_lang=target_lang)
    
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_path, 'w', encoding='utf-8') as of:
        json.dump(dic, of, ensure_ascii=False, indent=4)
    #遍历json内的所有对象
    

def translate_extern_file_through_dict(input_path,output_path,translated_json_path,included=['.json']):

    for dir_path,_, files in tqdm(os.walk(input_path)):
        for file in tqdm(files):
            suffix=os.path.splitext(file)[1]
            if suffix in included:
                if suffix=='.json':
                    translate_json_througn_dict(os.path.join(dir_path, file),os.path.join(output_path,dir_path,file),translated_json_path,'ja','zh-cn')
                if suffix=='.csv':
                    translate_Database_through_dict(os.path.join(dir_path, file),translated_json_path,os.path.join(output_path,dir_path,file),override=False)
if __name__ == '__main__':
    included=['.json']
    input_path='sugorokuDatas'
    translated_json_path='翻译_本体_DLC_fixed.json'
    output_path='output_t'
    translate_extern_file_through_dict(input_path,output_path,translated_json_path,included)