package com.example.cahil.myapplication;

import android.support.v4.app.FragmentActivity;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class Map extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        Bundle extras = getIntent().getExtras();
        String rlat = extras.getString("RLAT");
        String rlng = extras.getString("RLNG");
        String clat = extras.getString("CLAT");
        String clng = extras.getString("CLNG");

        double restlat = Double.parseDouble(rlat);
        double restlng = Double.parseDouble(rlng);
        double custlat = Double.parseDouble(clat);
        double custlng = Double.parseDouble(clng);

        // Add a marker in Sydney and move the camera
        LatLng restaurant = new LatLng(restlat, restlng);
        LatLng customer = new LatLng(custlat, custlng);
        mMap.addMarker(new MarkerOptions().position(restaurant).title("Restaurant"));
        mMap.addMarker(new MarkerOptions().position(customer).title("Customer"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(restaurant));

    }
}
