package com.example.cahil.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import android.widget.EditText;
import android.widget.TextView;


public class Main3Activity extends AppCompatActivity {
    private TextView orderNumber = null;
    private TextView restaurantName = null;
    private TextView customerName = null;
    private TextView restaurantLat = null;
    private TextView restaurantLng = null;
    private TextView customerLat = null;
    private TextView customerLng = null;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        orderNumber   = (TextView)findViewById(R.id.textView1);
        orderNumber.setText("1");
        restaurantName   = (TextView)findViewById(R.id.textView2);
        restaurantName.setText("Pizza Hut");
        customerName   = (TextView)findViewById(R.id.textView3);
        customerName.setText("Mr Customer");
        restaurantLat   = (TextView)findViewById(R.id.textView4);
        restaurantLat.setText("52.7765");
        restaurantLng   = (TextView)findViewById(R.id.textView5);
        restaurantLng.setText("-6.9341");
        customerLat   = (TextView)findViewById(R.id.textView6);
        customerLat.setText("52.7234");
        customerLng   = (TextView)findViewById(R.id.textView7);
        customerLng.setText("-6.8234");

        Button yourButton = findViewById(R.id.button1);

        yourButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                String rlat = restaurantLat.getText().toString();
                String rlng = restaurantLng.getText().toString();
                String clat = customerLat.getText().toString();
                String clng = customerLng.getText().toString();

                Intent intent = new Intent(Main3Activity.this, Map.class);
                Bundle extras = new Bundle();
                extras.putString("RLAT",rlat);
                extras.putString("RLNG",rlng);
                extras.putString("CLAT",clat);
                extras.putString("CLNG",clng);
                intent.putExtras(extras);
                startActivity(intent);

            }
        });
        Button myButton = findViewById(R.id.button2);

        myButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){




                startActivity(new Intent(Main3Activity.this, Main2Activity.class));



            }
        });



    }
}
