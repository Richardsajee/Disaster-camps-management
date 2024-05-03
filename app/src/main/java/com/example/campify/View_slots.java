package com.example.campify;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class View_slots extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_slots);

//        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
//        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
//                new Response.Listener<String>() {
//                    @Override
//                    public void onResponse(String response) {
//                        //  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();
//
//                        // response
//                        try {
//                            JSONObject jsonObj = new JSONObject(response);
//                            if (jsonObj.getString("status").equalsIgnoreCase("ok")) {
//
//                                JSONArray js= jsonObj.getJSONArray("users");
//                                list=new String[js.length()];
//                                quantity=new String[js.length()];
//                                camp=new String[js.length()];
//                                volunter=new String[js.length()];
//                                phone=new String[js.length()];
//                                latitude=new String[js.length()];
//                                longitude=new String[js.length()];
////                                type=new String[js.length()];
////                                discription=new String[js.length()];
////                                image=new String[js.length()];
////                                status=new String[js.length()];
////
////                                JSONArray js1= jsonObj.getJSONArray("rating");
////                                rating=new String[js1.length()];
//
//                                for(int i=0;i<js.length();i++)
//                                {
//                                    JSONObject u=js.getJSONObject(i);
//                                    list[i]=u.getString("list");
//                                    quantity[i]=u.getString("quantityt");
//                                    camp[i]=u.getString("camp");
//                                    volunter[i]=u.getString("name");
//                                    phone[i]=u.getString("phone");
//                                    latitude[i]=u.getString("latitude");
//                                    longitude[i]=u.getString("longitude");
////                                    type[i]=u.getString("type");
////                                    discription[i]=u.getString("description");
////                                    image[i]=u.getString("image");
////                                    status[i]=u.getString("status");
//
//
//                                }
////                                for(int i=0;i<js1.length();i++)
////                                {
////                                    JSONObject u=js1.getJSONObject(i);
////                                    rating[i]=u.getString("rating");
////
////                                }
//
//                                // ArrayAdapter<String> adpt=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,name);
//                                listView.setAdapter(new customviewneeds(getApplicationContext(),list,quantity, camp, volunter, phone,latitude,longitude));
//                                // l1.setAdapter(new Custom(getApplicationContext(),gamecode,name,type,discription,image,status));
//                            }
//
//
//                            // }
//                            else {
//                                Toast.makeText(getApplicationContext(), "Not found", Toast.LENGTH_LONG).show();
//                            }
//
//                        }    catch (Exception e) {
//                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
//                        }
//                    }
//                },
//                new Response.ErrorListener() {
//                    @Override
//                    public void onErrorResponse(VolleyError error) {
//                        // error
//                        Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
//                    }
//                }
//        ) {
//            @Override
//            protected Map<String, String> getParams() {
//                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//                Map<String, String> params = new HashMap<String, String>();
//
//                String id=sh.getString("uid","");
//                params.put("uid",id);
////                params.put("mac",maclis);
//
//                return params;
//            }
//        };
//
//        int MY_SOCKET_TIMEOUT_MS=100000;
//
//        postRequest.setRetryPolicy(new DefaultRetryPolicy(
//                MY_SOCKET_TIMEOUT_MS,
//                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
//                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
//        requestQueue.add(postRequest);
    }
}