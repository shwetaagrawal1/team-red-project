package com.example.cfit010.contact_app;

import android.content.Context;
import android.os.AsyncTask;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by cfit010 on 19/7/16.
 */
public class RequestTask extends AsyncTask<String, Void, String> {

    private TextView textData;
    private Context context;
    private String json_data;


    public RequestTask(Context context,TextView textData,String json_data) {
        this.context = context;
        this.textData = textData;
        this.json_data = json_data;
    }





    @Override
    protected String doInBackground(String... uri) {
        HttpURLConnection conn = null;
            try {

                URL url = new URL(uri[0]);//"http://192.168.3.10:8000/create_contact"
                 conn = (HttpURLConnection) url.openConnection();
                conn.setDoOutput(true);
                conn.setRequestMethod("POST");
                conn.setRequestProperty("Content-Type", "application/json");

                String input = 	json_data; //"{\"name\":\"ss\",\"city\":\"bhopal\",\"number\":\"52564354663\",\"email\":\"ssaa@gmail.com\"}";

                System.out.println(input);

                OutputStream os = conn.getOutputStream();
                os.write(input.getBytes());
                os.flush();

			/*if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
			throw new RuntimeException("Failed : HTTP error code : "
				+ conn.getResponseCode());
		}*/

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));

                String output = null;
                System.out.println("Output from Server .... \n");

                String result = "";

                //AddContactActivity.this



            while ((output = br.readLine()) != null) {
                System.out.println(output);
                result = result+output;
            }
                return result;
            } catch (MalformedURLException e) {

                e.printStackTrace();

            } catch (IOException e) {
                e.printStackTrace();

            }
            finally {
                conn.disconnect();
            }
            return  "error";
    }

    @Override
    protected void onPostExecute(String result) {
        this.textData.setText(result);
    }
}
