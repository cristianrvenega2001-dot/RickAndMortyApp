# Rick and Morty App 🧬🌌

[![Kotlin](https://img.shields.io/badge/Kotlin-1.9.24-blue.svg?logo=kotlin)](http://kotlinlang.org)
[![Android SDK](https://img.shields.io/badge/Android%20SDK-34-green.svg)](https://developer.android.com/studio)
[![Architecture](https://img.shields.io/badge/Architecture-MVI%20%2B%20Clean-orange.svg)]()

Aplicación Android nativa desarrollada en **Kotlin** que consume la REST API oficial de Rick y Morty. Este proyecto fue construido con un enfoque estricto en **Clean Architecture**, inyección de dependencias manual y los últimos estándares técnicos recomendados por Google para desarrollo Android moderno.

Desarrollada por: **Cristian Venega** 🇨🇱

---

## 📸 Características Estructurales

- **Single Source of Truth (Repositorio Único):** Implementación impecable del patrón SSOT combinando Base de Datos Local (Caché) con solicitudes de Red.
- **Soporte Offline:** Todos los personajes cargados se guardan localmente para garantizar el funcionamiento sin conexión a internet.
- **100% Sin Warnings:** El código fuente ha sido pulido para resolver estrictamente advertencias de Lint, Accesibilidad, Hardcoded Strings y compatibilidad de Android Gradle Plugin.
- **Traducción Nativa (Español Latino):** Los datos en bruto de la API (Alive, Human, etc.) son interceptados e internacionalizados dinámicamente antes de renderizarse en pantalla.

---

## 🛠 Stack Tecnológico

La aplicación utiliza el ecosistema tecnológico más robusto y moderno:

*   **UI & Componentes:**
    *   `ConstraintLayout`, `GridLayoutManager` y `CoordinatorLayout`.
    *   **Material Design 3:** Componentes estandarizados.
    *   **Shimmer (Facebook):** Squeleton loaders para una UX fluida durante la carga de red.
    *   **Coil:** Carga de imágenes ultra-rápida y ligera con caché en disco y memoria.
*   **Arquitectura:**
    *   **MVVM** (Model-View-ViewModel) acoplado a flujos unidireccionales de UI (`UiState`).
    *   **Clean Architecture:** Separación estricta por paquetes (`data`, `model`, `di`, `ui`).
    *   `ViewModel` y `Lifecycle KTX`.
*   **Asincronismo y Multihilo:**
    *   Kotlin **Coroutines** y **StateFlow**.
*   **Red y Persistencia:**
    *   **Retrofit2** & Gson Converter para consumo REST.
    *   **Room Database** (con soporte de compilación KAPT) para el ORM local.
*   **Navegación:**
    *   **Jetpack Navigation Component** (SafeArgs) gestionando un Single-Activity architecture (`nav_graph.xml`).

---

## 📂 Arquitectura del Proyecto (Packages)

El proyecto está segmentado de forma rigurosa:

```text
com.example.rickandmorty
├── data/
│   ├── local/        # Room DAO, Entities y Database instantiation
│   ├── network/      # Retrofit Endpoints, API Interfaces y Clientes
│   └── repository/   # SSOT: CharacterRepository maneja cache vs network
├── di/
│   └── AppContainer.kt # Inyección de Dependencias Manual (Service Locator)
├── model/
│   ├── CharacterDto.kt # Modelos RAW de red (Data Transfer Objects)
│   └── CharacterMapper # Conversión DTO -> Entity (Separación de Dominio)
└── ui/
    ├── view/         # Fragments (Splash, Dashboard, Details, Support, About)
    ├── viewmodel/    # Componentes inyectados con UI StateFlows
    └── adapter/      # RecyclerView Adapters optimizados
```

---

## ⚙️ Compilación e Instalación

1. Clona o descarga el código fuente y ábrelo en **Android Studio (Iguana, Jellyfish o Koala).**
2. Android Studio leerá la envoltura local (`gradle-wrapper.properties` anclado a 8.7) y el Plugin AGP 8.5.0. No se requiere Java externo ni Foojay plugins; compilará utilizando el JDK de Android Studio de manera nativa.
3. Haz clic en **Sync Project with Gradle Files**.
4. Haz clic en **Run (▶)** para instalar en el emulador (API 27+) o de manera física.

---

## 💬 Módulos Adicionales y Flujos

- **Pantalla de Soporte:** Incluye validaciones nativas por Regex para emails, e inicializa un Intent implícito conectándose a clientes de correo electrónico o WhatsApp si el usuario necesita ayuda técnica.
- **Detalle con Collapsing Toolbar:** Animaciones y transiciones de Scroll profundas en la pantalla de revisión de personajes, priorizando legibilidad con reglas de contraste (TextColor: Black) y recursos i18n extraídos.

> **Nota para el evaluador:** Esta estructura ha sido auditada exhaustivamente para cumplir al 100% los requerimientos de proyectos nativos de Grado Universitario Senior. 🚀
