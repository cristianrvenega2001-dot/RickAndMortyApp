package com.example.rickandmorty.di

import android.content.Context
import com.example.rickandmorty.data.local.AppDatabase
import com.example.rickandmorty.data.network.RetrofitInstance
import com.example.rickandmorty.data.repository.CharacterRepository

class AppContainer(context: Context) {
    private val db = AppDatabase.getDatabase(context)
    private val characterDao = db.characterDao()
    private val apiService = RetrofitInstance.api

    val characterRepository: CharacterRepository by lazy {
        CharacterRepository(apiService, characterDao)
    }
}
