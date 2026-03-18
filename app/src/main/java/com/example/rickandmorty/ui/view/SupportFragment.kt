package com.example.rickandmorty.ui.view

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.example.rickandmorty.R
import com.example.rickandmorty.databinding.FragmentSupportBinding

class SupportFragment : Fragment(R.layout.fragment_support) {
    private lateinit var binding: FragmentSupportBinding

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding = FragmentSupportBinding.bind(view)

        binding.btnSendReport.setOnClickListener {
            validateAndSend()
        }
    }

    private fun validateAndSend() {
        val name = binding.edtName.text.toString()
        val email = binding.edtEmail.text.toString()
        val message = binding.edtMessage.text.toString()

        if (name.isEmpty() || email.isEmpty() || message.isEmpty()) {
            Toast.makeText(context, getString(R.string.toast_fill_fields), Toast.LENGTH_SHORT).show()
            return
        }

        if (!android.util.Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            binding.edtEmail.error = getString(R.string.error_invalid_email)
            return
        }

        sendEmail(name, message)
    }

    private fun sendEmail(name: String, message: String) {
        val intent = Intent(Intent.ACTION_SENDTO).apply {
            data = Uri.parse("mailto:")
            putExtra(Intent.EXTRA_EMAIL, arrayOf(getString(R.string.support_email)))
            putExtra(Intent.EXTRA_SUBJECT, getString(R.string.support_subject, name))
            putExtra(Intent.EXTRA_TEXT, message)
        }
        
        if (intent.resolveActivity(requireActivity().packageManager) != null) {
            startActivity(intent)
        } else {
            sendWhatsApp(message)
        }
    }

    private fun sendWhatsApp(message: String) {
        val intent = Intent(Intent.ACTION_VIEW).apply {
            data = Uri.parse("https://wa.me/123456789?text=${Uri.encode(message)}")
        }
        startActivity(intent)
    }
}
