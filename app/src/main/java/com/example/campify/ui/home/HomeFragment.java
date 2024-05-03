package com.example.campify.ui.home;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.example.campify.Locationservice;
import com.example.campify.R;
import com.example.campify.customviewalertmessage;
import com.example.campify.customviewnearestcamp;
import com.example.campify.customviewprecaution;
import com.example.campify.databinding.FragmentHomeBinding;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class HomeFragment extends Fragment {
    String[] alert;
    TextView textView24,textView25,textView26,textView27;

    ListView listView;
    SharedPreferences sh;
    ProgressDialog pd;

    private FragmentHomeBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        HomeViewModel homeViewModel =
                new ViewModelProvider(this).get(HomeViewModel.class);

        binding = FragmentHomeBinding.inflate(inflater, container, false);
        View root = binding.getRoot();

        sh = PreferenceManager.getDefaultSharedPreferences(getContext());
        listView = root.findViewById(R.id.list);
        textView24 = root.findViewById(R.id.textView24);
        textView25 = root.findViewById(R.id.textView25);
        textView26 = root.findViewById(R.id.textView26);
        textView27 = root.findViewById(R.id.textView27);

        String url = sh.getString("url", "")+"/viewalerts";




        pd = new ProgressDialog(getContext());
        pd.setMessage("Fetching....");
        pd.show();
        RequestQueue requestQueue = Volley.newRequestQueue(getContext());
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        //  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                        // response
                        try {
                            pd.dismiss();
                            JSONObject jsonObj = new JSONObject(response);
                            if (jsonObj.getString("status").equalsIgnoreCase("ok")) {

                                textView24.setText(jsonObj.getString("city"));
                                textView25.setText(jsonObj.getString("temp"));
                                textView26.setText(jsonObj.getString("description"));
                                textView27.setText(jsonObj.getString("wind"));



                                JSONArray js= jsonObj.getJSONArray("data");
                                alert=new String[js.length()];

//                                type=new String[js.length()];
//                                discription=new String[js.length()];
//                                image=new String[js.length()];
//                                status=new String[js.length()];
//
//                                JSONArray js1= jsonObj.getJSONArray("rating");
//                                rating=new String[js1.length()];

                                for(int i=0;i<js.length();i++)
                                {
                                    JSONObject u=js.getJSONObject(i);
                                    alert[i]=u.getString("alert");


//                                    type[i]=u.getString("type");
//                                    discription[i]=u.getString("description");
//                                    image[i]=u.getString("image");
//                                    status[i]=u.getString("status");


                                }
//                                for(int i=0;i<js1.length();i++)
//                                {
//                                    JSONObject u=js1.getJSONObject(i);
//                                    rating[i]=u.getString("rating");
//
//                                }

                                // ArrayAdapter<String> adpt=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,name);
                                listView.setAdapter(new customviewalertmessage(getContext(),alert));
                                // l1.setAdapter(new Custom(getApplicationContext(),gamecode,name,type,discription,image,status));
                            }


                            // }
                            else {
                                Toast.makeText(getContext(), "Not found", Toast.LENGTH_LONG).show();
                            }

                        }    catch (Exception e) {
                            Toast.makeText(getContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<String, String>();
                params.put("latitude", Locationservice.lati);
                params.put("longitude", Locationservice.logi);
                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS=100000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);




        return root;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}