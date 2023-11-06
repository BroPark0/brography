package com.nable.testec2;

import com.android.volley.AuthFailureError;
import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class SignupRequestActivity extends StringRequest {

    final static private String URL = "http://3.39.222.94/signup_test.php";
    private Map<String, String> map;

    public SignupRequestActivity(String ID, String Password, Response.Listener<String> listener)
    {
        super(Method.POST, URL, listener, null);

        map = new HashMap<>();
        map.put("ID", ID);
        map.put("Password", Password);
    }

    @Override
    protected Map<String, String> getParams() throws AuthFailureError {
        return map;
    }
}
