package com.example.campify;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.TextView;

public class customviewneeds extends BaseAdapter {
    String[] list,quantity, camp, volunteer, phone,latitude,longitude;
    Context context;

    public customviewneeds(Context applicationContext, String[] list, String[] quantity, String[] camp, String[] volunteer, String[] phone, String[] latitude, String[] longitude) {
        this.context = applicationContext;
        this.list = list;
        this.quantity = quantity;
        this.camp = camp;
        this.volunteer = volunteer;
        this.phone = phone;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    @Override
    public int getCount() {
        return list.length;
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
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.activity_customviewneeds,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView21);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView22);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView13);
        TextView tv4=(TextView)gridView.findViewById(R.id.textView19);
        Button locate = gridView.findViewById(R.id.button3);
        Button call = gridView.findViewById(R.id.button4);

        tv1.setText(list[i]);
        tv2.setText(quantity[i]);
        tv3.setText(camp[i]);
        tv4.setText(volunteer[i]);


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

        call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent phone_intent = new Intent(Intent.ACTION_CALL);
                phone_intent.setData(Uri.parse("tel:"+phone[i]));
                phone_intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(phone_intent);

            }
        });



        return gridView;
    }
}