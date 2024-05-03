package com.example.campify;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.VideoView;

public class customviewprecaution extends BaseAdapter {
    String[] description, file;
    Context context;

    public customviewprecaution(Context applicationContext, String[] description, String[] file) {
        this.file = file;
        this.description = description;
        this.context = applicationContext;


    }


    @Override
    public int getCount() {
        return description.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null){
            gridView = new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView = inflator.inflate(R.layout.activity_customviewprecaution, null);

        }
        else

        {
            gridView = (View) view;

        }

        TextView tv1 = (TextView) gridView.findViewById(R.id.textView23);
        VideoView videoView = (VideoView) gridView.findViewById(R.id.videoView);
        Button btn = gridView.findViewById(R.id.button6);

        tv1.setText(description[i]);

        ///VV1.
        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
        String path = sh.getString("url", "")+file[i];

        Uri uri = Uri.parse(path);

        videoView.setVideoURI(uri);


        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               if( btn.getText().toString().equalsIgnoreCase("Play")){
                   videoView.start();
                   btn.setText("Pause");
               }
               else {
                   videoView.pause();
                   btn.setText("Play");
               }

            }
        });



//        MediaController mediaController = new MediaController(context);
//        mediaController.setAnchorView(VV1);
//        mediaController.setMediaPlayer(VV1);
////
//        Uri uri = Uri.parse(path);
//        VV1.setVideoURI(uri);
//        VV1.setMediaController(mediaController);
//        VV1.start();

        return gridView;
    }

}
