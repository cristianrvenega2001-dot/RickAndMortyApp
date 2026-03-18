package com.example.rickandmorty.model

import com.example.rickandmorty.data.local.CharacterEntity

fun CharacterDto.toEntity(): CharacterEntity {
    return CharacterEntity(
        id = this.id,
        name = this.name,
        status = this.status,
        species = this.species,
        image = this.image,
        gender = this.gender
    )
}
