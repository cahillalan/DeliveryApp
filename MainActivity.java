package com.example.cahil.myapplication;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.content.Intent;
import android.widget.EditText;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {
    private EditText inputtext;
    private EditText inputtext2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputtext   = (EditText)findViewById(R.id.input1);
        inputtext2 = (EditText)findViewById(R.id.input2);

        Button yourButton = findViewById(R.id.button1);

        yourButton.setOnClickListener(new OnClickListener(){
            public void onClick(View v){


                String password = inputtext2.getText().toString();
                String username = inputtext.getText().toString();
                String pass = "open";
                String user = "Driver";

                if(inputtext.getText().toString().equals("user") &&
                        inputtext2.getText().toString().equals("pass")  ) {
                    startActivity(new Intent(MainActivity.this, Main2Activity.class));
                } else{
                    Toast.makeText(getApplicationContext(), "Wrong UserName or Password", Toast.LENGTH_LONG).show();

                }


            }
        });

    }



}
