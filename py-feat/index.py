# from feat import Detector
# from feat import Fex
#
# # wrapper around face, landmark, au, emotions. etc models
# detector = Detector()
# # performs all types of detections on image
# detector.detect_image('/Users/qozeemodeniran/Desktop/avatar.png')
#
# # special dataframe that stores and operates on detector output
# fex = Fex()

from feat import Detector, Fex

detector = Detector(au_model='svm', emotion_model='resmasknet')

# return a Fex dataclass
detections = detector.detect_image('/Users/qozeemodeniran/Desktop/avatar.png')

detections.head()
# detections.regress(X=my_design_matrix, y=detections.aus)