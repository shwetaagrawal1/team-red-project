package com.example.cfit010.contact_app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by cfit010 on 19/7/16.
 */
public class FormActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.form);
    }

    public void openConatctActivity(View view) {
        Intent intent = new Intent(FormActivity.this, AddContactActivity.class);
        EditText name = (EditText) findViewById(R.id.editName);
        EditText number = (EditText) findViewById(R.id.editNumber);
        EditText email = (EditText) findViewById(R.id.editEmail);
        EditText city = (EditText) findViewById(R.id.editCity);
        JSONObject obj = new JSONObject();
        try {
            obj.put("name", name.getText().toString());
            obj.put("number", number.getText().toString());
            obj.put("email", email.getText().toString());
            obj.put("city", city.getText().toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        intent.putExtra("json",obj.toString());
        String method = getIntent().getStringExtra("method");
        intent.putExtra("method",method);
        startActivity(intent);
    }

}
