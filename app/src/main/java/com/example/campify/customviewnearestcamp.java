package com.example.campify;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.TextView;

public class customviewnearestcamp extends BaseAdapter {
    String[] name,latitude,longitude, slot;
    Context context;


    public customviewnearestcamp(Context applicationContext, String[] name, String[] latitude, String[] longitude, String[] slot) {
        this.context = applicationContext;
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
        this.slot = slot;
    }

    public customviewnearestcamp(Context context, String[] alert) {
    }

    @Override
    public int getCount() {
        return name.length;
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
        if (view == null) {
            gridView = new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView = inflator.inflate(R.layout.activity_customviewnearestcamp, null);

        } else {
            gridView = (View) view;

        }
        TextView tname = (TextView) gridView.findViewById(R.id.textView11);
        Button locate = gridView.findViewById(R.id.button);
        TextView tslot = gridView.findViewById(R.id.textView29);


        tname.setText(name[i]);
        tslot.setText("Slot: "+slot[i]);
        locate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent j = new Intent(Intent.ACTION_VIEW, Uri.parse("http://maps.google.com/maps?q=loc:" + latitude[i] + "," + longitude[i]));
                j.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK); // Only if initiating from a Broadcast Receiver
                String mapsPackageName = "com.google.android.apps.maps";
                j.setClassName(mapsPackageName, "com.google.android.maps.MapsActivity");
                j.setPackage(mapsPackageName);
                context.startActivity(j);


            }
        });


        return gridView;


    }
}