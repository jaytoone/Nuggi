import os
import sys
import json
import datetime
import numpy as np
import itertools

balloon_json_path = 'samples/balloon/datasets/balloon/train/via_region_data.json'
gogi_json_path = 'samples/gogi/via_region_data.json'
gogi_json_train_path = 'samples/gogi/datasets/multiple_gogi/train/via_region_data.json'
gogi_json_val_path = 'samples/gogi/datasets/multiple_gogi/val/via_region_data.json'

annotations = json.load(open(balloon_json_path))
annotations_ = json.load(open(gogi_json_path))

# print((annotations_.keys()))
annotations_train = dict()
annotations_val = dict()
for key in (list(annotations_)[:6]):
    annotations_train[key] = annotations_[key]
for key in (list(annotations_)[6:]):
    annotations_val[key] = annotations_[key]

# print(annotations_)
# print(annotations_train)
# annotations_val = dict(itertools.islice(annotations_.items(), 6))

#       save file       #
with open(gogi_json_train_path, "w") as json_file:
    json.dump(annotations_train, json_file)
with open(gogi_json_val_path, "w") as json_file:
    json.dump(annotations_val, json_file)
quit()


#       delete keys         #
# del annotations_['test1.jpg8578']
# del annotations_['ahimsa_DSC048912.jpg112544']
# print(annotations_['ahimsa_DSC048912.jpg112544'])




annotations_list = list(annotations.values())  # don't need the dict keys
annotations_list_ = list(annotations_.values()) #[1:][0]  # don't need the dict keys

# key_names = list(annotations_list_.keys())
# for i in range(len(annotations_list_)):
#     annotations_list_[i] = annotations_list_[key_names[i]]

# print(annotations_list[0])
# print()
# print()
# print()
for i, diction in enumerate(annotations_list_):

    if diction['filename'] in ['ahimsa_DSC048912.jpg', 'test1.jpg']:
        del annotations_list_[i]

for i, diction in enumerate(annotations_list_):

    print(diction['filename'])

print(len(annotations_))
quit()

#   list 의 모양을 동일하게 만들어준다
# for i in range(len(annotations_list_)):
#     # print(annotations_list_[i]['regions'][0])
#     # quit()
#     i = 59
#     print(annotations_list_[i]['regions'])
#     annotations_list_[i]['regions'] = {'0': annotations_list_[i]['regions'][0]}
#     print(annotations_list_[i])
#     # quit()
# # print(annotations_list_[0])
#
# quit()
#
# annotations_a = [a for a in annotations_list if a['regions']]
# annotations_a_ = [a for a in annotations_list_ if a['regions']]
#
# print(annotations_a[0])
# print(annotations_a_[0])
# quit()
# for i in range(len(annotations)):
#     print(annotations[i])
#     break
#


