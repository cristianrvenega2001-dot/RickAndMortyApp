package com.example.rickandmorty.ui.view

import android.os.Bundle
import androidx.lifecycle.SavedStateHandle
import androidx.navigation.NavArgs
import java.lang.IllegalArgumentException
import kotlin.Int
import kotlin.jvm.JvmStatic

public data class DetailsFragmentArgs(
  public val characterId: Int = -1,
) : NavArgs {
  public fun toBundle(): Bundle {
    val result = Bundle()
    result.putInt("characterId", this.characterId)
    return result
  }

  public fun toSavedStateHandle(): SavedStateHandle {
    val result = SavedStateHandle()
    result.set("characterId", this.characterId)
    return result
  }

  public companion object {
    @JvmStatic
    public fun fromBundle(bundle: Bundle): DetailsFragmentArgs {
      bundle.setClassLoader(DetailsFragmentArgs::class.java.classLoader)
      val __characterId : Int
      if (bundle.containsKey("characterId")) {
        __characterId = bundle.getInt("characterId")
      } else {
        __characterId = -1
      }
      return DetailsFragmentArgs(__characterId)
    }

    @JvmStatic
    public fun fromSavedStateHandle(savedStateHandle: SavedStateHandle): DetailsFragmentArgs {
      val __characterId : Int?
      if (savedStateHandle.contains("characterId")) {
        __characterId = savedStateHandle["characterId"]
        if (__characterId == null) {
          throw IllegalArgumentException("Argument \"characterId\" of type integer does not support null values")
        }
      } else {
        __characterId = -1
      }
      return DetailsFragmentArgs(__characterId)
    }
  }
}
