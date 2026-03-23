package com.example.rickandmorty.data.repository;

@kotlin.Metadata(mv = {1, 9, 0}, k = 1, xi = 48, d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\u0018\u00002\u00020\u0001B\u0015\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\u0006\u0010\u0004\u001a\u00020\u0005\u00a2\u0006\u0002\u0010\u0006J\u0018\u0010\u0007\u001a\u0004\u0018\u00010\b2\u0006\u0010\t\u001a\u00020\nH\u0086@\u00a2\u0006\u0002\u0010\u000bJ2\u0010\f\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\b0\u000e0\r2\n\b\u0002\u0010\u000f\u001a\u0004\u0018\u00010\u00102\n\b\u0002\u0010\u0011\u001a\u0004\u0018\u00010\u0010H\u0086@\u00a2\u0006\u0002\u0010\u0012R\u000e\u0010\u0002\u001a\u00020\u0003X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u0004\u001a\u00020\u0005X\u0082\u0004\u00a2\u0006\u0002\n\u0000\u00a8\u0006\u0013"}, d2 = {"Lcom/example/rickandmorty/data/repository/CharacterRepository;", "", "apiService", "Lcom/example/rickandmorty/data/network/RickAndMortyApiService;", "characterDao", "Lcom/example/rickandmorty/data/local/CharacterDao;", "(Lcom/example/rickandmorty/data/network/RickAndMortyApiService;Lcom/example/rickandmorty/data/local/CharacterDao;)V", "getCharacterById", "Lcom/example/rickandmorty/data/local/CharacterEntity;", "id", "", "(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;", "getCharacters", "Lkotlinx/coroutines/flow/Flow;", "", "status", "", "species", "(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "app_debug"})
public final class CharacterRepository {
    @org.jetbrains.annotations.NotNull()
    private final com.example.rickandmorty.data.network.RickAndMortyApiService apiService = null;
    @org.jetbrains.annotations.NotNull()
    private final com.example.rickandmorty.data.local.CharacterDao characterDao = null;
    
    public CharacterRepository(@org.jetbrains.annotations.NotNull()
    com.example.rickandmorty.data.network.RickAndMortyApiService apiService, @org.jetbrains.annotations.NotNull()
    com.example.rickandmorty.data.local.CharacterDao characterDao) {
        super();
    }
    
    @org.jetbrains.annotations.Nullable()
    public final java.lang.Object getCharacterById(int id, @org.jetbrains.annotations.NotNull()
    kotlin.coroutines.Continuation<? super com.example.rickandmorty.data.local.CharacterEntity> $completion) {
        return null;
    }
    
    @org.jetbrains.annotations.Nullable()
    public final java.lang.Object getCharacters(@org.jetbrains.annotations.Nullable()
    java.lang.String status, @org.jetbrains.annotations.Nullable()
    java.lang.String species, @org.jetbrains.annotations.NotNull()
    kotlin.coroutines.Continuation<? super kotlinx.coroutines.flow.Flow<? extends java.util.List<com.example.rickandmorty.data.local.CharacterEntity>>> $completion) {
        return null;
    }
}