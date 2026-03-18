package com.example.rickandmorty.model

data class CharacterResponseDto(
    val results: List<CharacterDto>
)

data class CharacterDto(
    val id: Int,
    val name: String,
    val status: String,
    val species: String,
    val type: String,
    val gender: String,
    val image: String,
    val url: String,
    val created: String
)
