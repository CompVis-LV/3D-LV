
bool PlaneDetection::readDepthImage(string filename)
{
    cv::Mat depth_img = cv::imread(filename, cv::IMREAD_ANYDEPTH);

    if(depth.type() != CV_32FC1)
        depth.convertTo(depth, CV_32FC1);

    // filters
    Mat_<float> f1 = (Mat_<float>(3, 3) << 1,  2,  1,
                                            0,  0,  0,
                                            -1, -2, -1) / 8;

    Mat_<float> f2 = (Mat_<float>(3, 3) << 1, 0, -1,
                                            2, 0, -2,
                                            1, 0, -1) / 8;

    /* Other filters that could be used:
    % f1 = [0, 0, 0;
    %       0, 1, 1;
    %       0,-1,-1]/4;
    % 
    % f2 = [0, 0, 0;
    %       0, 1,-1;
    %       0, 1,-1]/4;

    or

    % f1 = [0, 1, 0;
    %       0, 0, 0;
    %       0,-1, 0]/2;
    % 
    % f2 = [0, 0, 0;
    %       1, 0, -1;
    %       0, 0, 0]/2;
    */


    Mat f1m, f2m;
    flip(f1, f1m, 0);
    flip(f2, f2m, 1);

    Mat n1, n2;
    filter2D(depth, n1, -1, f1m, Point(-1, -1), 0, BORDER_CONSTANT);
    filter2D(depth, n2, -1, f2m, Point(-1, -1), 0, BORDER_CONSTANT);

    n1 *= -1;
    n2 *= -1;

    Mat temp = n1.mul(n1) + n2.mul(n2) + 1;
    cv::sqrt(temp, temp);

    Mat N3 = 1 / temp;
    Mat N1 = n1.mul(N3);
    Mat N2 = n2.mul(N3);

    vector<Mat> N;
    N.push_back(N1);
    N.push_back(N2);
    N.push_back(N3);

    Mat surface_normals;
    merge(N, surface_normals);

    imshow("convolution_based_normals", surface_normals);
}