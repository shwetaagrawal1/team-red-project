package com.example.cfit010.contact_app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by cfit010 on 20/7/16.
 */
public class FieldValueActivity extends Activity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.field_value);
    }
    public void openDataActivity(View view) {
        Intent intent = new Intent(FieldValueActivity.this, GetRequestActivity.class);
        EditText field_e = (EditText) findViewById(R.id.field);
        EditText value_e = (EditText) findViewById(R.id.value);
        String field = field_e.getText().toString();
        String value = value_e.getText().toString();

        String method = getIntent().getStringExtra("method");
        if(method.equals("delete_number"))
        {
            intent.putExtra("method", method+"/"+value);
        }
        else if(method.equals("get_filter"))
        {
            intent.putExtra("method", method+"/"+field+"="+value);
        }
        else if(method.equals("get_contact_details"))
        {
            intent.putExtra("method", method+"/"+value);
        }
        else if(method.equals("get_field_directory"))
        {
            intent.putExtra("method", method+"/"+field+"="+value);
        }
        else if(method.equals("get_provider_name"))
        {
            intent.putExtra("method", method+"/"+value);
        }
        else if(method.equals("get_records_of_provider"))
        {
            intent.putExtra("method", method+"/"+value);
        }

        startActivity(intent);
    }
}
