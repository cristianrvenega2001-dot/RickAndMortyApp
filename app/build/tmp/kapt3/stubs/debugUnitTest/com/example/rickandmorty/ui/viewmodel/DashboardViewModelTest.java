package com.example.rickandmorty.ui.viewmodel;

@kotlin.Metadata(mv = {1, 9, 0}, k = 1, xi = 48, d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0007\u0018\u00002\u00020\u0001B\u0005\u00a2\u0006\u0002\u0010\u0002J\f\u0010\t\u001a\u00060\nj\u0002`\u000bH\u0007J\b\u0010\f\u001a\u00020\nH\u0007J\b\u0010\r\u001a\u00020\nH\u0007R\u0012\u0010\u0003\u001a\u00020\u00048\u0002@\u0002X\u0083.\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u0005\u001a\u00020\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u0007\u001a\u00020\bX\u0082.\u00a2\u0006\u0002\n\u0000\u00a8\u0006\u000e"}, d2 = {"Lcom/example/rickandmorty/ui/viewmodel/DashboardViewModelTest;", "", "()V", "repository", "Lcom/example/rickandmorty/data/repository/CharacterRepository;", "testDispatcher", "Lkotlinx/coroutines/test/TestDispatcher;", "viewModel", "Lcom/example/rickandmorty/ui/viewmodel/DashboardViewModel;", "cuando el repositorio entrega datos, el estado cambia a Success", "", "Lkotlinx/coroutines/test/TestResult;", "setup", "tearDown", "app_debugUnitTest"})
@kotlinx.coroutines.ExperimentalCoroutinesApi()
public final class DashboardViewModelTest {
    @org.mockito.Mock()
    private com.example.rickandmorty.data.repository.CharacterRepository repository;
    private com.example.rickandmorty.ui.viewmodel.DashboardViewModel viewModel;
    @org.jetbrains.annotations.NotNull()
    private final kotlinx.coroutines.test.TestDispatcher testDispatcher = null;
    
    public DashboardViewModelTest() {
        super();
    }
    
    @org.junit.Before()
    public final void setup() {
    }
    
    @org.junit.After()
    public final void tearDown() {
    }
}