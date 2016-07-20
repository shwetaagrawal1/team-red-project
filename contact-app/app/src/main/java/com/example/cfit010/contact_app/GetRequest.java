package com.example.cfit010.contact_app;

import android.content.Context;
import android.os.AsyncTask;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by cfit010 on 19/7/16.
 */
public class GetRequest extends AsyncTask<String, Void, String> {

    private TextView textData;
    private Context context;


    public GetRequest(Context context,TextView textData) {
        this.context = context;
        this.textData = textData;
    }

    @Override
    protected String doInBackground(String... uri) {

        HttpURLConnection conn = null;
        try {

            URL url = new URL(uri[0]);//http://127.0.0.1:5000/ //http://www.httpbin.org/get
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Accept", "application/json");

            if (conn.getResponseCode() != 201) {
                throw new RuntimeException("Failed : HTTP error code : "
                        + conn.getResponseCode());
            }


            BufferedReader br = new BufferedReader(new InputStreamReader(
                    (conn.getInputStream())));

            String output;
            String result="";
            System.out.println("Output from Server .... \n");
            while ((output = br.readLine()) != null) {
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

        return "error";
    }

    @Override
    protected void onPostExecute(String result) {
        this.textData.setText(result);
    }

}
