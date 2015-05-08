#include <stdio.h>
#include <stdlib.h>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "opencv.h"

int detectAndDisplay(char* img)
{
    using namespace std;
    using namespace cv;

    string face_cascade_name = "./haarcascade_frontalface_alt.xml";
    CascadeClassifier face_cascade;

//Load the cascade
    if (!face_cascade.load(face_cascade_name))
    {
        printf("--(!)Error loading\n");
        return (-1);
    };
    
    Mat frame = imread(img);

    std::vector<Rect> faces;
    Mat frame_gray;
    Mat crop;
    Mat res;
    Mat gray;
    string text;
    stringstream sstm;

    cvtColor(frame, frame_gray, COLOR_BGR2GRAY);
    equalizeHist(frame_gray, frame_gray);

    // Detect faces
    face_cascade.detectMultiScale(frame_gray, faces, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));
     	
    return faces.size();  //añadido para mostrar el numero de caras detectadas

}
