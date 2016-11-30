function    ret =   fun_process(filestr)

    [filePath, fileName, fileExt]   =   fileparts(filestr);
    disp(filestr);

    % load decoded audio and video frames from .mat file.
    load(fullfile(filePath, [fileName, '.mat']));

    % audio play demo, should be removed in submitted version.
    fun_play_audio(audio);
    
    % video play demo. should be removed in submitted version.
    fun_play_video(video);
    
    ret_set =   {'Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise'};
    if (exist('fun_classification.m', 'file'))
        ret_val =   fun_classification(filestr);
    else
        warning('No available classification function. Random result returned.');
        ret_val =   randi([0, 6]);
    end
    ret =   ret_set{ret_val + 1};

end

function    fun_play_video(video)

    disp('Video information (note: totalDuration is not accurate, use times or frames for length evaluation):');
    disp(video);

    figure;
    hold on;
    imshow(video.frames(1).cdata);
    for i   =   2 : video.nrFramesTotal
        t_head  =   tic;
        pause(video.times(i) - video.times(i - 1) - toc(t_head));

        hold on;
        hold off;
        imshow(video.frames(i).cdata);
    end

end

function    fun_play_audio(audio)

    disp('Audio information (note: totalDuration is not accurate, use times or frames for length evaluation):');
    disp(audio);

    sound(audio.data, audio.rate);

end
