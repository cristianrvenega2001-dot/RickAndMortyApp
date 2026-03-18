package com.example.rickandmorty.ui.view

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.GridLayoutManager
import com.example.rickandmorty.R
import com.example.rickandmorty.RickAndMortyApp
import com.example.rickandmorty.databinding.FragmentDashboardBinding
import com.example.rickandmorty.ui.view.adapter.CharacterAdapter
import com.example.rickandmorty.ui.viewmodel.DashboardViewModel
import com.example.rickandmorty.ui.viewmodel.UiState
import kotlinx.coroutines.launch

class DashboardFragment : Fragment(R.layout.fragment_dashboard) {
    private lateinit var binding: FragmentDashboardBinding
    private lateinit var viewModel: DashboardViewModel
    private lateinit var adapter: CharacterAdapter

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding = FragmentDashboardBinding.bind(view)
        
        val app = requireActivity().application as RickAndMortyApp
        viewModel = DashboardViewModel(app.container.characterRepository)

        setupRecyclerView()
        observeState()
        
        binding.btnSupport.setOnClickListener {
            findNavController().navigate(R.id.action_dashboard_to_support)
        }
        
        binding.btnAbout.setOnClickListener {
            findNavController().navigate(R.id.action_dashboard_to_about)
        }
    }

    private fun setupRecyclerView() {
        adapter = CharacterAdapter { character ->
            val bundle = Bundle().apply {
                putInt("characterId", character.id)
            }
            findNavController().navigate(R.id.action_dashboard_to_details, bundle)
        }
        binding.recyclerView.apply {
            layoutManager = GridLayoutManager(context, 2)
            this.adapter = this@DashboardFragment.adapter
        }
    }

    private fun observeState() {
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.uiState.collect { state ->
                    when (state) {
                        is UiState.Loading -> {
                            binding.shimmerLayout.startShimmer()
                            binding.shimmerLayout.visibility = View.VISIBLE
                            binding.recyclerView.visibility = View.GONE
                        }
                        is UiState.Success -> {
                            binding.shimmerLayout.stopShimmer()
                            binding.shimmerLayout.visibility = View.GONE
                            binding.recyclerView.visibility = View.VISIBLE
                            adapter.submitList(state.data)
                        }
                        is UiState.Error -> {
                            binding.shimmerLayout.stopShimmer()
                        }
                    }
                }
            }
        }
    }
}
