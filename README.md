# Backstory Contenidos — nueva web

Versión integral en desarrollo: 30 páginas en español e inglés, nueve casos y una propuesta editorial basada en «Primero, la historia».

## Archivos

- `dist/`: web completa, lista para un alojamiento estático. Abrir `dist/index.html` para recorrerla localmente.
- `build.py` y `portfolio_updates.py`: contenido y generación de páginas.
- `dist/style.css` y `dist/site.js`: diseño e interacciones.
- `check_site.py`: comprobación estática de páginas y enlaces.
- `backstory-source.zip`: copia inicial importada; los archivos editables son la fuente de trabajo vigente.

## Reconstruir y comprobar

```sh
python3 build.py
python3 check_site.py
node --check dist/site.js
```

No requiere dependencias de frontend. El formulario prepara un correo; no envía datos automáticamente. La indexación está deshabilitada para esta revisión y los metadatos apuntan a la vista previa de GitHub Pages.

## Estado

La importación y las comprobaciones estáticas se ejecutaron en GitHub. El reporte registra 30 páginas, 862 referencias y cero errores detectados. No equivale a una auditoría completa de accesibilidad ni a una revisión visual integral.

El repositorio es público por autorización del propietario. Vista previa publicada: https://bernabebotte-beep.github.io/backstory-web/ . El despliegue se completó y se comprobó la carga y apariencia de la portada en escritorio. La revisión integral de páginas e interacciones, y la revisión móvil, siguen pendientes. La web del dominio original no fue modificada.

La acción `Import website source` se utilizó para importar el ZIP inicial. No volver a ejecutarla después de editar el sitio: restauraría los archivos de ese paquete. El trabajo posterior debe realizarse sobre los archivos editables.
