package com.example.rickandmorty.ui.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.rickandmorty.data.local.CharacterEntity
import com.example.rickandmorty.data.repository.CharacterRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.launch

sealed class UiState {
    object Loading : UiState()
    data class Success(val data: List<CharacterEntity>) : UiState()
    data class Error(val message: String) : UiState()
}

class DashboardViewModel(private val repository: CharacterRepository) : ViewModel() {

    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState

    init {
        fetchCharacters()
    }

    fun fetchCharacters(status: String? = null) {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            repository.getCharacters(status)
                .catch { _uiState.value = UiState.Error(it.message ?: "Error desconocido") }
                .collect { _uiState.value = UiState.Success(it) }
        }
    }
}
