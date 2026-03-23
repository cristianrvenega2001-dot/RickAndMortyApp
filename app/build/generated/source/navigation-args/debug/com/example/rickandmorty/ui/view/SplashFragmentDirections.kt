package com.example.rickandmorty.ui.view

import androidx.navigation.ActionOnlyNavDirections
import androidx.navigation.NavDirections
import com.example.rickandmorty.R

public class SplashFragmentDirections private constructor() {
  public companion object {
    public fun actionSplashToDashboard(): NavDirections =
        ActionOnlyNavDirections(R.id.action_splash_to_dashboard)
  }
}
