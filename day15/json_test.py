#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import json
import pickle
yangli = {'name': 'yangli', 'age': 73, 'gender': 'renyao', 'hobby': 'feiji', 'height': 20, }
# json_yangli = json.dumps(yangli)
#
# print(json_yangli)
#
# with open('a.json', 'w', encoding='utf-8') as f:
#     json.dump(json_yangli, f)
#
# with open('a.json', 'r', encoding='utf-8') as f:
#     res = json.load(f)
#     print(res)
#
#






res = pickle.dumps(yangli)
with open('tt.pkl','wb')as f:
    pickle.dump(res,f)
with open("tt.pkl",'rb')as f:
    d = pickle.load(f)

    print(pickle.loads(d))

