package com.example.rickandmorty

import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.contrib.RecyclerViewActions
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.example.rickandmorty.ui.view.adapter.CharacterAdapter
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class DashboardFlowTest {

    @get:Rule
    val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun verficar_navegacion_al_detalle() {
        Thread.sleep(3000) 
        onView(withId(R.id.recyclerView)).check(matches(isDisplayed()))
        onView(withId(R.id.recyclerView))
            .perform(RecyclerViewActions.actionOnItemAtPosition<CharacterAdapter.ViewHolder>(0, click()))
        onView(withId(R.id.collapsingToolbar)).check(matches(isDisplayed()))
    }
}
