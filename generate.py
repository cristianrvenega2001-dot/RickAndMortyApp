import os

project_root = r"C:\users\usuario\AndroidStudioProjects\rickandmortyapp"

files = {
    r"app\build.gradle": """plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
    id 'kotlin-kapt'
    id 'androidx.navigation.safeargs.kotlin'
}

android {
    namespace 'com.example.rickandmorty'
    compileSdk 34

    defaultConfig {
        applicationId "com.example.rickandmorty"
        minSdk 27
        targetSdk 34
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
    buildFeatures {
        viewBinding true
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = '17'
    }
}

dependencies {
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'

    // Navigation
    implementation "androidx.navigation:navigation-fragment-ktx:2.7.7"
    implementation "androidx.navigation:navigation-ui-ktx:2.7.7"

    // Room
    implementation "androidx.room:room-runtime:2.6.1"
    implementation "androidx.room:room-ktx:2.6.1"
    kapt "androidx.room:room-compiler:2.6.1"

    // Networking (Retrofit + GSON)
    implementation "com.squareup.retrofit2:retrofit:2.9.0"
    implementation "com.squareup.retrofit2:converter-gson:2.9.0"

    // UI & Media
    implementation "io.coil-kt:coil:2.5.0"
    implementation "com.facebook.shimmer:shimmer:0.5.0"
    implementation "com.google.android.material:material:1.11.0"

    // Lifecycle & Coroutines
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.7.0"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.7.0"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3"

    // Testing
    testImplementation "junit:junit:4.13.2"
    testImplementation "org.mockito:mockito-core:5.8.0"
    testImplementation "org.jetbrains.kotlinx:kotlinx-coroutines-test:1.7.3"
    androidTestImplementation "androidx.test.ext:junit:1.1.5"
    androidTestImplementation "androidx.test.espresso:espresso-core:3.5.1"
    androidTestImplementation "androidx.test.espresso:espresso-contrib:3.5.1"
}
""",
    r"app\src\main\AndroidManifest.xml": """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.rickandmorty">

    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

    <application
        android:name=".RickAndMortyApp"
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.RickAndMorty">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""",
    r"app\src\main\res\values\colors.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="primary">#4CAF50</color>
    <color name="primary_dark">#388E3C</color>
    <color name="accent">#FF9800</color>
    <color name="white">#FFFFFF</color>
    <color name="shimmer_base">#E0E0E0</color>
    <color name="shimmer_highlight">#F5F5F5</color>
</resources>""",
    r"app\src\main\res\values\themes.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.RickAndMorty" parent="Theme.Material3.DayNight.NoActionBar">
        <item name="colorPrimary">@color/primary</item>
        <item name="colorPrimaryDark">@color/primary_dark</item>
        <item name="colorAccent">@color/accent</item>
    </style>
</resources>""",
    r"app\src\main\res\values\strings.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Rick and Morty App</string>
</resources>""",
    r"app\src\main\res\navigation\nav_graph.xml": """<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/nav_graph"
    app:startDestination="@id/splashFragment">

    <fragment android:id="@+id/splashFragment" android:name="com.example.rickandmorty.ui.view.SplashFragment">
        <action android:id="@+id/action_splash_to_dashboard" app:destination="@id/dashboardFragment" app:popUpTo="@id/splashFragment" app:popUpToInclusive="true"/>
    </fragment>

    <fragment android:id="@+id/dashboardFragment" android:name="com.example.rickandmorty.ui.view.DashboardFragment">
        <action android:id="@+id/action_dashboard_to_details" app:destination="@id/detailsFragment" />
        <action android:id="@+id/action_dashboard_to_support" app:destination="@id/supportFragment" />
    </fragment>

    <fragment android:id="@+id/detailsFragment" android:name="com.example.rickandmorty.ui.view.DetailsFragment">
        <argument android:name="characterId" app:argType="integer" android:defaultValue="-1"/>
    </fragment>
    
    <fragment android:id="@+id/supportFragment" android:name="com.example.rickandmorty.ui.view.SupportFragment" />
</navigation>""",
    r"app\src\main\java\com\example\rickandmorty\MainActivity.kt": """package com.example.rickandmorty

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}""",
    r"app\src\main\res\layout\activity_main.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.fragment.app.FragmentContainerView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/nav_host_fragment"
    android:name="androidx.navigation.fragment.NavHostFragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:defaultNavHost="true"
    app:navGraph="@navigation/nav_graph" />""",
    r"app\src\main\java\com\example\rickandmorty\RickAndMortyApp.kt": """package com.example.rickandmorty

import android.app.Application
import com.example.rickandmorty.di.AppContainer

class RickAndMortyApp : Application() {
    lateinit var container: AppContainer

    override fun onCreate() {
        super.onCreate()
        container = AppContainer(this)
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\di\AppContainer.kt": """package com.example.rickandmorty.di

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
}""",
    r"app\src\main\java\com\example\rickandmorty\data\local\AppDatabase.kt": """package com.example.rickandmorty.data.local

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [CharacterEntity::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {
    abstract fun characterDao(): CharacterDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        fun getDatabase(context: Context): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "rick_morty_db"
                ).build()
                INSTANCE = instance
                instance
            }
        }
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\data\local\CharacterDao.kt": """package com.example.rickandmorty.data.local

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

@Dao
interface CharacterDao {
    @Query("SELECT * FROM characters")
    suspend fun getAllCharacters(): List<CharacterEntity>

    @Query("SELECT * FROM characters WHERE status = :status")
    suspend fun getCharactersByStatus(status: String): List<CharacterEntity>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertCharacters(characters: List<CharacterEntity>)

    @Query("DELETE FROM characters")
    suspend fun clearAll()
}""",
    r"app\src\main\java\com\example\rickandmorty\data\local\CharacterEntity.kt": """package com.example.rickandmorty.data.local

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "characters")
data class CharacterEntity(
    @PrimaryKey val id: Int,
    val name: String,
    val status: String,
    val species: String,
    val image: String,
    val gender: String
)""",
    r"app\src\main\java\com\example\rickandmorty\data\network\RetrofitInstance.kt": """package com.example.rickandmorty.data.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitInstance {
    private const val BASE_URL = "https://rickandmortyapi.com/api/"

    val api: RickAndMortyApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(RickAndMortyApiService::class.java)
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\data\network\RickAndMortyApiService.kt": """package com.example.rickandmorty.data.network

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
}""",
    r"app\src\main\java\com\example\rickandmorty\data\repository\CharacterRepository.kt": """package com.example.rickandmorty.data.repository

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
}""",
    r"app\src\main\java\com\example\rickandmorty\model\CharacterDto.kt": """package com.example.rickandmorty.model

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
)""",
    r"app\src\main\java\com\example\rickandmorty\model\CharacterMapper.kt": """package com.example.rickandmorty.model

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
}""",
    r"app\src\main\java\com\example\rickandmorty\ui\view\SplashFragment.kt": """package com.example.rickandmorty.ui.view

import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.View
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.rickandmorty.R

class SplashFragment : Fragment(R.layout.fragment_splash) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        Handler(Looper.getMainLooper()).postDelayed({
            findNavController().navigate(R.id.action_splash_to_dashboard)
        }, 2000)
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\ui\view\DashboardFragment.kt": """package com.example.rickandmorty.ui.view

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.GridLayoutManager
import com.example.rickandmorty.R
import com.example.rickandmorty.RickAndMortyApp
import com.example.rickandmorty.databinding.FragmentDashboardBinding
import com.example.rickandmorty.ui.view.adapter.CharacterAdapter
import com.example.rickandmorty.ui.viewmodel.DashboardViewModel
import com.example.rickandmorty.ui.viewmodel.UiState
import kotlinx.coroutines.launch

class DashboardFragment : Fragment(R.layout.fragment_dashboard) {
    private lateinit var binding: FragmentDashboardBinding
    private lateinit var viewModel: DashboardViewModel
    private lateinit var adapter: CharacterAdapter

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding = FragmentDashboardBinding.bind(view)
        
        val app = requireActivity().application as RickAndMortyApp
        viewModel = DashboardViewModel(app.container.characterRepository)

        setupRecyclerView()
        observeState()
        
        binding.btnSupport.setOnClickListener {
            findNavController().navigate(R.id.action_dashboard_to_support)
        }
    }

    private fun setupRecyclerView() {
        adapter = CharacterAdapter { character ->
            val bundle = Bundle().apply {
                putInt("characterId", character.id)
            }
            findNavController().navigate(R.id.action_dashboard_to_details, bundle)
        }
        binding.recyclerView.apply {
            layoutManager = GridLayoutManager(context, 2)
            this.adapter = this@DashboardFragment.adapter
        }
    }

    private fun observeState() {
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.uiState.collect { state ->
                    when (state) {
                        is UiState.Loading -> {
                            binding.shimmerLayout.startShimmer()
                            binding.shimmerLayout.visibility = View.VISIBLE
                            binding.recyclerView.visibility = View.GONE
                        }
                        is UiState.Success -> {
                            binding.shimmerLayout.stopShimmer()
                            binding.shimmerLayout.visibility = View.GONE
                            binding.recyclerView.visibility = View.VISIBLE
                            adapter.submitList(state.data)
                        }
                        is UiState.Error -> {
                            binding.shimmerLayout.stopShimmer()
                        }
                    }
                }
            }
        }
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\ui\view\DetailsFragment.kt": """package com.example.rickandmorty.ui.view

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import coil.load
import com.example.rickandmorty.R
import com.example.rickandmorty.databinding.FragmentDetailsBinding

class DetailsFragment : Fragment(R.layout.fragment_details) {
    private lateinit var binding: FragmentDetailsBinding

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding = FragmentDetailsBinding.bind(view)
        setupUI()
    }

    private fun setupUI() {
        binding.collapsingToolbar.title = "Rick Sanchez"
        binding.txtStatus.text = "Status: Alive"
        binding.txtSpecies.text = "Species: Human"
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\ui\view\SupportFragment.kt": """package com.example.rickandmorty.ui.view

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.example.rickandmorty.R
import com.example.rickandmorty.databinding.FragmentSupportBinding

class SupportFragment : Fragment(R.layout.fragment_support) {
    private lateinit var binding: FragmentSupportBinding

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding = FragmentSupportBinding.bind(view)

        binding.btnSendReport.setOnClickListener {
            validateAndSend()
        }
    }

    private fun validateAndSend() {
        val name = binding.edtName.text.toString()
        val email = binding.edtEmail.text.toString()
        val message = binding.edtMessage.text.toString()

        if (name.isEmpty() || email.isEmpty() || message.isEmpty()) {
            Toast.makeText(context, "Por favor completa todos los campos", Toast.LENGTH_SHORT).show()
            return
        }

        if (!android.util.Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            binding.edtEmail.error = "Email no válido"
            return
        }

        sendEmail(name, message)
    }

    private fun sendEmail(name: String, message: String) {
        val intent = Intent(Intent.ACTION_SENDTO).apply {
            data = Uri.parse("mailto:")
            putExtra(Intent.EXTRA_EMAIL, arrayOf("soporte@rickmorty.com"))
            putExtra(Intent.EXTRA_SUBJECT, "Soporte App - $name")
            putExtra(Intent.EXTRA_TEXT, message)
        }
        
        if (intent.resolveActivity(requireActivity().packageManager) != null) {
            startActivity(intent)
        } else {
            sendWhatsApp(message)
        }
    }

    private fun sendWhatsApp(message: String) {
        val intent = Intent(Intent.ACTION_VIEW).apply {
            data = Uri.parse("https://wa.me/123456789?text=${Uri.encode(message)}")
        }
        startActivity(intent)
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\ui\view\adapter\CharacterAdapter.kt": """package com.example.rickandmorty.ui.view.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import coil.load
import com.example.rickandmorty.data.local.CharacterEntity
import com.example.rickandmorty.databinding.ItemCharacterBinding

class CharacterAdapter(private val onClick: (CharacterEntity) -> Unit) :
    ListAdapter<CharacterEntity, CharacterAdapter.ViewHolder>(DiffCallback) {

    class ViewHolder(private val binding: ItemCharacterBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(item: CharacterEntity, onClick: (CharacterEntity) -> Unit) {
            binding.txtName.text = item.name
            binding.imgCharacter.load(item.image)
            binding.root.setOnClickListener { onClick(item) }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemCharacterBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position), onClick)
    }

    object DiffCallback : DiffUtil.ItemCallback<CharacterEntity>() {
        override fun areItemsTheSame(oldItem: CharacterEntity, newItem: CharacterEntity) = oldItem.id == newItem.id
        override fun areContentsTheSame(oldItem: CharacterEntity, newItem: CharacterEntity) = oldItem == newItem
    }
}""",
    r"app\src\main\java\com\example\rickandmorty\ui\viewmodel\DashboardViewModel.kt": """package com.example.rickandmorty.ui.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.rickandmorty.data.local.CharacterEntity
import com.example.rickandmorty.data.repository.CharacterRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.launch

sealed class UiState {
    object Loading : UiState()
    data class Success(val data: List<CharacterEntity>) : UiState()
    data class Error(val message: String) : UiState()
}

class DashboardViewModel(private val repository: CharacterRepository) : ViewModel() {

    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState

    init {
        fetchCharacters()
    }

    fun fetchCharacters(status: String? = null) {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            repository.getCharacters(status)
                .catch { _uiState.value = UiState.Error(it.message ?: "Error desconocido") }
                .collect { _uiState.value = UiState.Success(it) }
        }
    }
}""",
    r"app\src\main\res\layout\fragment_splash.xml": """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:background="?attr/colorPrimary">
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="¡Wubba Lubba Dub Dub!"
        android:textColor="@color/white"
        android:textSize="24sp"
        android:textStyle="bold"/>
</LinearLayout>""",
    r"app\src\main\res\layout\fragment_dashboard.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    <com.facebook.shimmer.ShimmerFrameLayout
        android:id="@+id/shimmerLayout"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">
            <View android:layout_width="match_parent" android:layout_height="200dp" android:background="@color/shimmer_base"/>
            <View android:layout_width="match_parent" android:layout_height="200dp" android:layout_marginTop="8dp" android:background="@color/shimmer_base"/>
        </LinearLayout>
    </com.facebook.shimmer.ShimmerFrameLayout>
    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:visibility="gone"/>
    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/btnSupport"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_margin="16dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:srcCompat="@android:drawable/ic_dialog_email" />
</androidx.constraintlayout.widget.ConstraintLayout>""",
    r"app\src\main\res\layout\item_character.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_margin="8dp"
    app:cardCornerRadius="8dp"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
        <ImageView
            android:id="@+id/imgCharacter"
            android:layout_width="match_parent"
            android:layout_height="150dp"
            android:scaleType="centerCrop" />
        <TextView
            android:id="@+id/txtName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:padding="8dp"
            android:textStyle="bold"
            android:textSize="16sp"/>
    </LinearLayout>
</androidx.cardview.widget.CardView>""",
    r"app\src\main\res\layout\fragment_details.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="300dp">
        <com.google.android.material.appbar.CollapsingToolbarLayout
            android:id="@+id/collapsingToolbar"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:layout_scrollFlags="scroll|exitUntilCollapsed"
            app:contentScrim="?attr/colorPrimary">
            <ImageView
                android:id="@+id/imgCharacterDetail"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:scaleType="centerCrop"
                app:layout_collapseMode="parallax" />
            <androidx.appcompat.widget.Toolbar
                android:layout_width="match_parent"
                android:layout_height="?attr/actionBarSize"
                app:layout_collapseMode="pin" />
        </com.google.android.material.appbar.CollapsingToolbarLayout>
    </com.google.android.material.appbar.AppBarLayout>
    <androidx.core.widget.NestedScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_behavior="@string/appbar_scrolling_view_behavior">
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="16dp">
            <TextView
                android:id="@+id/txtStatus"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="18sp"/>
            <TextView
                android:id="@+id/txtSpecies"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="18sp"
                android:layout_marginTop="8dp"/>
        </LinearLayout>
    </androidx.core.widget.NestedScrollView>
</androidx.coordinatorlayout.widget.CoordinatorLayout>""",
    r"app\src\main\res\layout\fragment_support.xml": """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">
    <EditText
        android:id="@+id/edtName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Nombre" />
    <EditText
        android:id="@+id/edtEmail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp"
        android:inputType="textEmailAddress"
        android:hint="Email" />
    <EditText
        android:id="@+id/edtMessage"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:layout_marginTop="8dp"
        android:gravity="top"
        android:hint="Mensaje de soporte" />
    <Button
        android:id="@+id/btnSendReport"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:text="Enviar Soporte" />
</LinearLayout>""",
    r"app\src\test\java\com\example\rickandmorty\ui\viewmodel\DashboardViewModelTest.kt": """package com.example.rickandmorty.ui.viewmodel

import com.example.rickandmorty.data.local.CharacterEntity
import com.example.rickandmorty.data.repository.CharacterRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.flowOf
import kotlinx.coroutines.test.*
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test
import org.mockito.Mock
import org.mockito.Mockito.`when`
import org.mockito.MockitoAnnotations

@ExperimentalCoroutinesApi
class DashboardViewModelTest {

    @Mock
    private lateinit var repository: CharacterRepository
    private lateinit var viewModel: DashboardViewModel
    
    private val testDispatcher = StandardTestDispatcher()

    @Before
    fun setup() {
        MockitoAnnotations.openMocks(this)
        Dispatchers.setMain(testDispatcher)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun `cuando el repositorio entrega datos, el estado cambia a Success`() = runTest {
        val mockData = listOf(CharacterEntity(1, "Rick", "Alive", "Human", "", "Male"))
        `when`(repository.getCharacters()).thenReturn(flowOf(mockData))

        viewModel = DashboardViewModel(repository)
        advanceUntilIdle()

        val currentState = viewModel.uiState.value
        assert(currentState is UiState.Success)
        assertEquals(mockData, (currentState as UiState.Success).data)
    }
}""",
    r"app\src\androidTest\java\com\example\rickandmorty\DashboardFlowTest.kt": """package com.example.rickandmorty

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
}"""
}

for rel_path, content in files.items():
    full_path = os.path.join(project_root, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
print(f"Project saved entirely in {project_root}")
