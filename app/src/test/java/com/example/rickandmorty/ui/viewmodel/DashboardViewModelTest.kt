package com.example.rickandmorty.ui.viewmodel

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
}
