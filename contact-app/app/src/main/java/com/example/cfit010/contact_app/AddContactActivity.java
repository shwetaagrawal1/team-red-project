package com.example.cfit010.contact_app;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.widget.TextView;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by cfit010 on 18/7/16.
 */
public class AddContactActivity extends Activity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.conatct_activity);
        TextView text = (TextView)findViewById(R.id.text);
        String json_data= getIntent().getStringExtra("json");
        String method = getIntent().getStringExtra("method");
        System.out.println(json_data);
        Log.d("idddd", "hrere" + json_data);
       // obj.toString();
        new RequestTask(this,text,json_data).execute("http://192.168.3.10:8000/"+method);//http://192.168.3.10:8000/create_contact
        //TextView text = (TextView)findViewById(R.id.text);
        //text.setText(result);


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.layout_two, menu);
        return true;
    }

}
