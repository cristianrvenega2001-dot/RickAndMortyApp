package com.example.rickandmorty.data.repository

import com.example.rickandmorty.data.local.CharacterDao
import com.example.rickandmorty.data.local.CharacterEntity
import com.example.rickandmorty.data.network.RickAndMortyApiService
import com.example.rickandmorty.model.toEntity
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow

class CharacterRepository(
    private val apiService: RickAndMortyApiService,
    private val characterDao: CharacterDao
) {
    suspend fun getCharacterById(id: Int): CharacterEntity? {
        return characterDao.getCharacterById(id)
    }
    suspend fun getCharacters(status: String? = null, species: String? = null): Flow<List<CharacterEntity>> = flow {
        val cached = if (status != null) {
            characterDao.getCharactersByStatus(status)
        } else {
            characterDao.getAllCharacters()
        }
        emit(cached)

        try {
            val response = apiService.getCharacters(status, species)
            if (response.isSuccessful) {
                val networkCharacters = response.body()?.results ?: emptyList()
                val entities = networkCharacters.map { it.toEntity() }
                characterDao.insertCharacters(entities)
                emit(entities)
            }
        } catch (e: Exception) {
            if (cached.isEmpty()) {
                throw e
            }
        }
    }
}
