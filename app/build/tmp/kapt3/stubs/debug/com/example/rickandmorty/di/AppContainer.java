package com.example.rickandmorty.di;

@kotlin.Metadata(mv = {1, 9, 0}, k = 1, xi = 48, d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u00a2\u0006\u0002\u0010\u0004R\u000e\u0010\u0005\u001a\u00020\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u0007\u001a\u00020\bX\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u001b\u0010\t\u001a\u00020\n8FX\u0086\u0084\u0002\u00a2\u0006\f\n\u0004\b\r\u0010\u000e\u001a\u0004\b\u000b\u0010\fR\u000e\u0010\u000f\u001a\u00020\u0010X\u0082\u0004\u00a2\u0006\u0002\n\u0000\u00a8\u0006\u0011"}, d2 = {"Lcom/example/rickandmorty/di/AppContainer;", "", "context", "Landroid/content/Context;", "(Landroid/content/Context;)V", "apiService", "Lcom/example/rickandmorty/data/network/RickAndMortyApiService;", "characterDao", "Lcom/example/rickandmorty/data/local/CharacterDao;", "characterRepository", "Lcom/example/rickandmorty/data/repository/CharacterRepository;", "getCharacterRepository", "()Lcom/example/rickandmorty/data/repository/CharacterRepository;", "characterRepository$delegate", "Lkotlin/Lazy;", "db", "Lcom/example/rickandmorty/data/local/AppDatabase;", "app_debug"})
public final class AppContainer {
    @org.jetbrains.annotations.NotNull()
    private final com.example.rickandmorty.data.local.AppDatabase db = null;
    @org.jetbrains.annotations.NotNull()
    private final com.example.rickandmorty.data.local.CharacterDao characterDao = null;
    @org.jetbrains.annotations.NotNull()
    private final com.example.rickandmorty.data.network.RickAndMortyApiService apiService = null;
    @org.jetbrains.annotations.NotNull()
    private final kotlin.Lazy characterRepository$delegate = null;
    
    public AppContainer(@org.jetbrains.annotations.NotNull()
    android.content.Context context) {
        super();
    }
    
    @org.jetbrains.annotations.NotNull()
    public final com.example.rickandmorty.data.repository.CharacterRepository getCharacterRepository() {
        return null;
    }
}