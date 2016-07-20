package com.example.cfit010.contact_app;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }


    public void openNewActivity(View view) {
        Intent intent = new Intent(this, FormActivity.class);
        intent.putExtra("method","create_contact");
        startActivity(intent);

    }

    public void openModifyActivity(View view) {
        Intent intent = new Intent(this, FormActivity.class);
        intent.putExtra("method","modify_contact");
        startActivity(intent);
    }

    public void openDisplayActivity(View view) {
        Intent intent = new Intent(this, GetRequestActivity.class);
        intent.putExtra("method","get_directory");
        startActivity(intent);
    }

    public void openDeleteActivity(View view) {
        Intent intent = new Intent(this, FieldValueActivity.class);
        intent.putExtra("method","delete_number");
        startActivity(intent);
    }

    public void openFilterActivity(View view) {
        Intent intent = new Intent(this, FieldValueActivity.class);
        intent.putExtra("method","get_filter");
        startActivity(intent);
    }

    public void openContactActivity(View view) {
        Intent intent = new Intent(this, FieldValueActivity.class);
        intent.putExtra("method","get_contact_details");
        startActivity(intent);
    }

    public void openFeildDirectoryActivity(View view) {
        Intent intent = new Intent(this, FieldValueActivity.class);
        intent.putExtra("method","get_field_directory");
        startActivity(intent);
    }

    public void openProviderActivity(View view) {
        Intent intent = new Intent(this, FieldValueActivity.class);
        intent.putExtra("method","get_provider_name");
        startActivity(intent);
    }

    public void openProviderRecordsActivity(View view) {
        Intent intent = new Intent(this, FieldValueActivity.class);
        intent.putExtra("method","get_records_of_provider");
        startActivity(intent);
    }

}
