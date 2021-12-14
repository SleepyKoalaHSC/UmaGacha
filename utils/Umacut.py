import cv2


def getVideoPng(videoPath, pngPath, frame):
    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print(fps)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (frame - 1) * 1000 / fps)
    success, image = vidcap.read()
    if success:
        print('ok')
        cv2.imwrite(pngPath, image)
        return


def cut(input_path, output_path, begin_frame, end_frame):
    videoCapture = cv2.VideoCapture(input_path)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (2340, 1080)
    videoWriter = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
    i = 0
    while True:
        success, frame = videoCapture.read()
        if success:
            i += 1
            if begin_frame <= i <= end_frame:
                videoWriter.write(frame)
        else:
            print(input_path + ' end')
            break
    videoCapture.release()


cut(r'H:\うまぴょい伝説\新建文件夹\1.特别周.mp4', 'output.avi', 1, 1405)
# fps = 30  # 保存视频的帧率
# size = (2340, 1080)  # 保存视频的大小
#
# videoWriter = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)
# i = 0
#
# while True:
#     success, frame = videoCapture.read()
#     if success:
#         i += 1
#         print('i = ', i)
#         if 1 <= i <= 960:
#             videoWriter.write(frame)
#     else:
#         print('end')
#         break
