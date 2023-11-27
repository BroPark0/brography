package com.nable.rcs_test_v20;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    EditText editText;
    TextView textView;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText = findViewById(R.id.edit_text);

        textView = findViewById(R.id.txt);


        //전달받은 Intent 객체 생성

        Intent intent = getIntent();

        //인텐트에 저장되어있는 데이터 추출
        String bankAccount = intent.getStringExtra("EXTRA_BANK_ACCOUNT");
        textView.setText(bankAccount);

//        Intent resultIntent = new Intent();
//        resultIntent.putExtra(EXTRA_PLUGIN_REQUEST_TYPE, 200);
//        ArrayList<Uri> uri = new ArrayList<>();
//        uri.add(“content uri”);
//        uri.add(“content uri”);
//        resultIntent.putParcelableArrayListExtra("EXTRA_PLUGIN_CONTENT_LIST", uri);
//        resultIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
//        resultIntent.setType(“image/jpg”);
//        getActivity().setResult(Activity.RESULT_OK, resultIntent);
    }

    //onclick event 메서드
    public void onclick(View view) {

//        // 1. 인텐트 생성
//        Intent intent = new Intent(MainActivity.this, MainActivity.class);
//
//        intent.putExtra("EXTRA_BANK_ACCOUNT",editText.getText().toString());  // 텍스트 읽어오기
//        //전달받은 Intent 객체 생성

        Intent intent = getIntent();

        //인텐트에 저장되어있는 데이터 추출
        String bankAccount = intent.getStringExtra("EXTRA_BANK_ACCOUNT");
        textView.setText(bankAccount);
        startActivity(intent);

        // 2. 실행할 엑티비티의 패키지 정보. 엑티비티 정보를 정의(설정)
//        ComponentName componentName = new ComponentName("com.nable.rcs_test_v20", "com.nable.rcs_test_v20.MainActivity");
//
//        // 3. Intent에 정보를 설정
//        intent.setComponent(componentName);
//
//        // 데이터를 전달하기 위해 intent에 데이터 저장
//        intent.putExtra("EXTRA_BANK_ACCOUNT", "Cool");
//
//        // 4. 액티비티 실행
//        startActivity(intent);

    }
}