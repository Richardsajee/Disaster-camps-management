package com.example.campify;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Funddonation extends AppCompatActivity {
    EditText fund, nm;
    Button pay;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_funddonation);
        fund = findViewById(R.id.editTextNumber2);
        nm = findViewById(R.id.editTextTextPersonName2);
        pay = findViewById(R.id.button5);

        pay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String amt = fund.getText().toString();
                String name = nm.getText().toString();

                startActivity(new Intent(getApplicationContext(), PaymentActivity.class).putExtra("amount", amt).putExtra("name", name));
            }
        });



    }
}