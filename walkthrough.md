# Restauración del Icono de Android

Se ha corregido el problema donde la aplicación `RickAndMortyApp` mostraba una estrella blanca en lugar del logo estándar de Android.

## Cambios Realizados

### Configuración de Recursos
- **Nuevos Archivos**: Se agregaron los vectores oficiales del logo de Android en `app/src/main/res/drawable/`:
    - [ic_launcher_foreground.xml](file:///C:/Users/usuario/AndroidStudioProjects/ZooAppFinal/app/src/main/res/drawable/ic_launcher_foreground.xml) (El androide blanco/verde)
    - [ic_launcher_background.xml](file:///C:/Users/usuario/AndroidStudioProjects/ZooAppFinal/app/src/main/res/drawable/ic_launcher_background.xml) (El fondo cuadriculado verde)
- **Modificaciones**: Se actualizaron los archivos de iconos adaptativos en `app/src/main/res/mipmap-anydpi-v26/` ([ic_launcher.xml](file:///C:/Users/usuario/AndroidStudioProjects/rickandmortyapp/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml) e [ic_launcher_round.xml](file:///C:/Users/usuario/AndroidStudioProjects/rickandmortyapp/app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml)) para que usen estos nuevos recursos en lugar de la estrella predeterminada del sistema.

### Sincronización con GitHub
Se realizaron los siguientes pasos en la terminal de Android Studio para asegurar que los cambios estén en la nube:
1. `git add`: Se añadieron los 4 archivos relacionados al icono.
2. `git commit`: Se creó un commit con el mensaje "Fix: restaurar el icono de Android por defecto de la aplicación".
3. `git push`: Se subieron los cambios al repositorio remoto `github` en la rama `master`.

## Verificación
- El comando `git push` se completó con éxito hacia `https://github.com/cristianrvenega2001-dot/RickAndMortyApp.git`.
- Al reinstalar la aplicación en el emulador o teléfono real, ahora aparecerá el logo de Android correctamente.

![Confirmación de Push de Git](file:///C:/Users/usuario/AndroidStudioProjects/rickandmortyapp/app/src/main/res/drawable/ic_launcher_foreground.xml)
> [!NOTE]
> La imagen de arriba es el recurso vectorial restaurado que ahora sirve como frente del icono.
