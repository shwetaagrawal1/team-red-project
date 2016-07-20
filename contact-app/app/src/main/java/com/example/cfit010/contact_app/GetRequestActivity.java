package com.example.cfit010.contact_app;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

/**
 * Created by cfit010 on 19/7/16.
 */
public class GetRequestActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.conatct_activity);
        TextView text = (TextView)findViewById(R.id.text);
        String method = getIntent().getStringExtra("method");
        new GetRequest(this,text).execute("http://192.168.3.10:8000/"+method);//http://192.168.3.10:8000/create_contact
    }


}
