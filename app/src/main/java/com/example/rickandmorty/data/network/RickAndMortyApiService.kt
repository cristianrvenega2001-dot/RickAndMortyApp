package com.example.rickandmorty.data.network

import com.example.rickandmorty.model.CharacterResponseDto
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Query

interface RickAndMortyApiService {
    @GET("character")
    suspend fun getCharacters(
        @Query("status") status: String? = null,
        @Query("species") species: String? = null
    ): Response<CharacterResponseDto>
}
