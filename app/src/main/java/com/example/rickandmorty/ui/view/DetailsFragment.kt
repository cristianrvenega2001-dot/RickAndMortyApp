package com.example.rickandmorty.ui.view

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.lifecycle.lifecycleScope
import coil.load
import com.example.rickandmorty.R
import com.example.rickandmorty.RickAndMortyApp
import com.example.rickandmorty.databinding.FragmentDetailsBinding
import kotlinx.coroutines.launch

class DetailsFragment : Fragment(R.layout.fragment_details) {
    private lateinit var binding: FragmentDetailsBinding

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding = FragmentDetailsBinding.bind(view)
        
        val characterId = arguments?.getInt("characterId", -1) ?: -1
        if (characterId != -1) {
            setupUI(characterId)
        }
    }

    private fun setupUI(characterId: Int) {
        val app = requireActivity().application as RickAndMortyApp
        val repository = app.container.characterRepository

        viewLifecycleOwner.lifecycleScope.launch {
            val character = repository.getCharacterById(characterId)
            character?.let {
                binding.collapsingToolbar.title = it.name
                
                binding.imgCharacterDetail.load(it.image) {
                    crossfade(true)
                }

                val statusEs = when (it.status.lowercase()) {
                    "alive" -> "Vivo"
                    "dead" -> "Muerto"
                    else -> "Desconocido"
                }

                val speciesEs = when (it.species.lowercase()) {
                    "human" -> "Humano"
                    "alien" -> "Alienígena"
                    "mythological creature" -> "Criatura Mitológica"
                    "animal" -> "Animal"
                    else -> it.species
                }

                val genderEs = when (it.gender.lowercase()) {
                    "male" -> "Masculino"
                    "female" -> "Femenino"
                    "genderless" -> "Sin género"
                    else -> "Desconocido"
                }

                binding.txtStatus.text = getString(R.string.status_template, statusEs)
                binding.txtSpecies.text = getString(R.string.species_template, speciesEs)
                binding.txtGender.text = getString(R.string.gender_template, genderEs)
            }
        }
    }
}
