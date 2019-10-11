import os,sys
import json
import shutil
from PIL import Image

labelname = 'to_label_hk_url.json'
srcfile = 'hk'
dstfile = 'crop/'+srcfile+'/'
labelfile = 'crop/'+srcfile+'_label/'


f = open(labelname,'r').read()
labels = json.loads(str(f))

if not os.path.exists(dstfile):
    os.mkdir(dstfile)

if not os.path.exists(labelfile):
    os.mkdir(labelfile)

print len(labels.keys())
for imgkey in labels.keys():
    print(labels[imgkey])
    try:
    # if 1:
        label = labels[imgkey]
        imgname = label['filename'].split('/')[-1].split('&')[0]

        if imgname == 'various_shapes.jpg' or imgname == 'eath_of_socrates_by_david.jpg' or imgname == 'death_of_socrates_by_david.jpg' or imgname == 'swan_in_geneve.jpg':
            continue
        # if not imgname[:6] == '_z-oss':
        #     continue
        regions = label['regions']
        # print regions
        if not regions:
            continue
        # print regions
        shape = regions[0]['shape_attributes']
        x = shape['all_points_x']
        y = shape['all_points_y']
        print x,y
        # print srcfile+imgname, dstfile+imgname
        shutil.copy(srcfile+'/'+imgname, dstfile+'/'+imgname)
        with open(labelfile+imgname+'.txt', 'w') as lf:
            print >> lf, x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3]
    except:
        pass
    # print shape



# alllist = os.listdir(srcfile)
# for filename in alllist:
#     im = Image.open(srcfile+filename)
#     w,h = im.size
#     shutil.copy(srcfile+filename, dstfile+filename)
#     with open(labelfile+filename+'.txt', 'w') as lf:
#             print >> lf, 0, 0, w, 0, w, h, 0, h





