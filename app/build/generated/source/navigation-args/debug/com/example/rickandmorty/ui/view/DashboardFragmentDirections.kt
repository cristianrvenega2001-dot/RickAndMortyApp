package com.example.rickandmorty.ui.view

import android.os.Bundle
import androidx.navigation.ActionOnlyNavDirections
import androidx.navigation.NavDirections
import com.example.rickandmorty.R
import kotlin.Int

public class DashboardFragmentDirections private constructor() {
  private data class ActionDashboardToDetails(
    public val characterId: Int = -1,
  ) : NavDirections {
    public override val actionId: Int = R.id.action_dashboard_to_details

    public override val arguments: Bundle
      get() {
        val result = Bundle()
        result.putInt("characterId", this.characterId)
        return result
      }
  }

  public companion object {
    public fun actionDashboardToDetails(characterId: Int = -1): NavDirections =
        ActionDashboardToDetails(characterId)

    public fun actionDashboardToSupport(): NavDirections =
        ActionOnlyNavDirections(R.id.action_dashboard_to_support)

    public fun actionDashboardToAbout(): NavDirections =
        ActionOnlyNavDirections(R.id.action_dashboard_to_about)
  }
}
