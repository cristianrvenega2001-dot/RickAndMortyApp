package com.example.rickandmorty

import android.app.Application
import com.example.rickandmorty.di.AppContainer

class RickAndMortyApp : Application() {
    lateinit var container: AppContainer

    override fun onCreate() {
        super.onCreate()
        container = AppContainer(this)
    }
}
