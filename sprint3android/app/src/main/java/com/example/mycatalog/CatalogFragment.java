package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.mycatalog.DetailActivity;

public class CatalogFragment extends Fragment {

    public CatalogFragment() {
        super(R.layout.fragment_catalog);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        Button btnDetalle = view.findViewById(R.id.btn_navegar_detalle);
        btnDetalle.setOnClickListener(v -> {
            Intent intent = new Intent(requireContext(), DetailActivity.class);
            startActivity(intent);
        });
    }
}
