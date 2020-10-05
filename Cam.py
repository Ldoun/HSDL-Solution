import sys
import cv2
import os
import time
sys.path.append('C:/Users/Lee/Documents/GitHub/HSDL-Solution/mask_detect/')
from tensorflow_infer import inference

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def play_vid(video_path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    conf_thresh=0.5
    cap = cv2.VideoCapture(video_path)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # writer = cv2.VideoWriter(output_video_name, fourcc, int(fps), (int(width), int(height)))
    out = cv2.VideoWriter(BASE_DIR+'/otter_out.mp4', fourcc, fps, (int(width), int(height)))
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    if not cap.isOpened():
        raise ValueError("Video open failed.")
        return
    status = True
    idx = 0
    while status:
        start_stamp = time.time()
        status, img_raw = cap.read()
        try:
            img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
        except:
            break
        read_frame_stamp = time.time()
        if (status):
            inference(img_raw,conf_thresh,iou_thresh=0.5,target_shape=(260, 260),draw_result=True,show_result=False)
            out.write(img_raw[:, :, ::-1])
            cv2.waitKey(1)
            inference_stamp = time.time()
            # writer.write(img_raw)
            write_frame_stamp = time.time()
            idx += 1
            print("%d of %d" % (idx, total_frames))
            print("read_frame:%f, infer time:%f, write time:%f" % (read_frame_stamp - start_stamp,
                                                                   inference_stamp - read_frame_stamp,
                                                                   write_frame_stamp - inference_stamp))

class Camera(object):
    '''def __init__(self):
        self.video_path="C:/workspace/Dangook_c/otter_out.mp4"
        self.frames=[]
        print(self.video_path)
        cap = cv2.VideoCapture(self.video_path)
        status=True
        while(status):
            status,frame=cap.read()
            try:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            except:
                break
            #cv2.imshow("img1",frame[:, :, ::-1])
            #print(frame[:, :, ::-1])
            self.frames.append(cv2.imencode('.jpg', frame)[1].tobytes())'''

    def __init__(self):
        lee=0
        ldh=0
        #self.video_path="C:/workspace/Dangook_c/otter_out.mp4"
        self.video_path="C:/Users/Lee/Desktop/a/dd.mp4"
        self.frames=[]
        self.peopleImageFolder="C:/Users/Lee/Desktop/a/people/"
        people=os.listdir(self.peopleImageFolder)

        
        name=[]
        for p in people:

            name.append(p[:-4])

        people=[self.peopleImageFolder+i for i in people]
        count={}
        for i in name:
            count[i]=0
        print(people)
        people_count=0
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        conf_thresh=0.5
        cap = cv2.VideoCapture(self.video_path)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #out = cv2.VideoWriter(BASE_DIR+'/otter_out.mp4', fourcc, fps, (int(width), int(height)))
        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        if not cap.isOpened():
            raise ValueError("Video open failed.")
            return
        status = True
        idx = 0
        while status:
            start_stamp = time.time()
            status, img_raw = cap.read()
            try:
                img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
            except:
                break
            read_frame_stamp = time.time()
            if (status):
                outinfo=inference(img_raw,people_count,people,name)
                #print(len(outinfo))
                people_count=len(outinfo)
                for info in outinfo:
                    print(info)
                    if(info[-1]!=''):
                        count[info[-1]]=count[info[-1]]+1

                
                #out.write(img_raw[:, :, ::-1])
                self.frames.append(cv2.imencode('.jpg', img_raw[:, :, ::-1])[1].tobytes())
                cv2.waitKey(1)
                inference_stamp = time.time()
                # writer.write(img_raw)
                write_frame_stamp = time.time()
                idx += 1
                print("%d of %d" % (idx, total_frames))
                print("read_frame:%f, infer time:%f, write time:%f" % (read_frame_stamp - start_stamp,
                                                                    inference_stamp - read_frame_stamp,
                                                                    write_frame_stamp - inference_stamp))                
        for i in count.keys():
            if(count[i]>0):
                print(i,end=" ")

        print('-----------------------------------------------------------------')

    def get_frame(self):  
        len(self.frames)           
        return  self.frames
       
#play_vid('C:/Users/Lee/Desktop/a/testvideo.mp4')