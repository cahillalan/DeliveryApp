package com.example.cahil.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Main2Activity extends AppCompatActivity {
    int clicks = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);




        Button yourButton = findViewById(R.id.button1);

        yourButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (clicks == 3) {
                    startActivity(new Intent(Main2Activity.this, Main3Activity.class));
                } else {
                    clicks += 1;
                    Toast.makeText(getApplicationContext(), "No Delivery's Available", Toast.LENGTH_LONG).show();

                }


            }


        });
    }
}
