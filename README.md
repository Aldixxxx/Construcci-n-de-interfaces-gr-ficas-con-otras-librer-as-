# 🐍 Flet: Interfaces gráficas con Python

---

## 📑 Tabla de contenido

1. [¿Qué es Flet?](#1-qué-es-flet)
2. [Aplicaciones que permite desarrollar](#2-aplicaciones-que-permite-desarrollar)
3. [Instalación y requisitos](#3-instalación-y-requisitos)
4. [Componentes principales](#4-componentes-principales)
5. [Manejo de eventos](#5-manejo-de-eventos)
6. [Ventajas frente a Tkinter](#6-ventajas-frente-a-tkinter)
7. [Limitaciones frente a Tkinter](#7-limitaciones-frente-a-tkinter)
8. [Ejemplo mínimo: contador interactivo](#8-ejemplo-mínimo-contador-interactivo)

---

## 1. ¿Qué es Flet?

**Flet** es un *framework* de Python para crear interfaces gráficas de aplicaciones de **escritorio**, **web** y **móviles**.

> 🎯 **Propósito principal:** permitir que los desarrolladores construyan interfaces visuales usando **solo Python**, sin necesidad de aprender HTML, CSS o JavaScript.

Flet utiliza **controles visuales**, que son elementos como:

- Textos
- Botones
- Campos de texto
- Contenedores
- Listas

Estos controles se organizan dentro de una **página principal** y pueden responder a acciones del usuario, como **clics**, **escritura** o **pulsaciones de teclado**.

---

## 2. Aplicaciones que permite desarrollar

Con Flet se pueden desarrollar aplicaciones para diferentes plataformas:

| Tipo de aplicación | Plataformas |
|--------------------|-------------|
| 🖥️ **Escritorio** | Windows, macOS y Linux |
| 🌐 **Web** | Cualquier navegador |
| 📱 **Móvil** | Android e iOS |

### Alcance de los proyectos

- **Aplicaciones sencillas:** un contador, una calculadora o un formulario.
- **Aplicaciones completas:** con varias pantallas, menús e interacción con datos.

---

## 3. Instalación y requisitos

### ✅ Requisito

| Requisito | Versión |
|-----------|---------|
| **Python** | 3.10 o superior |

### 📦 Instalación

Se recomienda crear un **entorno virtual** y ejecutar el siguiente comando:

```bash
pip install flet[all]
```

### ¿Qué instala este comando?

- La **biblioteca principal** de Flet.
- La **herramienta de línea de comandos** (CLI).
- Los **clientes necesarios** para ejecutar aplicaciones de escritorio y web.

---

## 4. Componentes principales

Los componentes principales de Flet se llaman **controles**.

| Control | Descripción |
|---------|-------------|
| `Page` | El más importante: representa la **ventana o pantalla principal** de la aplicación. |
| `Text` | Muestra **texto** en pantalla. |
| `Button` | Crea **botones** que responden cuando el usuario hace clic. |
| `Container` | Organiza otros elementos y aplica estilos como **color, tamaño, borde o alineación**. |
| `Row` | Organiza los elementos de forma **horizontal**. |
| `Column` | Organiza los elementos de forma **vertical**. |
| `TextField` | Permite al usuario **escribir texto**. |
| `FloatingActionButton` | Muestra un **botón flotante**, normalmente usado para la **acción principal**. |

---

## 5. Manejo de eventos

Flet maneja los eventos mediante propiedades como **`on_click`**.

### ⚙️ ¿Cómo funciona?

1. La propiedad `on_click` se asigna a un control, normalmente un **botón**.
2. Recibe el **nombre de una función** que se ejecutará cuando ocurra la interacción.
3. Cuando el usuario hace clic, Flet **llama automáticamente** a esa función.
4. La función puede recibir un parámetro llamado **`e`**, que representa el **evento** generado por el usuario.

### 🔄 ¿Qué se puede hacer dentro de la función?

- Modificar valores.
- Cambiar textos.
- Agregar elementos.
- Actualizar la interfaz.

> ⚠️ **Importante:** para que los cambios sean visibles, normalmente se llama al método **`page.update()`**.

---

## 6. Ventajas frente a Tkinter

- ✅ **Multiplataforma:** permite desarrollar para escritorio, web y móvil, mientras que Tkinter está orientado principalmente a escritorio.
- ✅ **Apariencia moderna:** está basado en **Flutter**.
- ✅ **Sin HTML, CSS ni JavaScript:** las interfaces se crean solo con Python.
- ✅ **Mismo código en distintos entornos:** facilita la creación de aplicaciones multiplataforma.

---

## 7. Limitaciones frente a Tkinter

- ❌ **Versión de Python:** Flet requiere Python **3.10 o superior**; Tkinter puede funcionar con versiones anteriores.
- ❌ **Mayor peso:** puede ser más pesado para programas muy pequeños, ya que incluye herramientas y componentes adicionales. Tkinter suele ser más **ligero y sencillo** para aplicaciones básicas de escritorio.
- ❌ **Curva de aprendizaje:** tiene una **estructura y sintaxis propias**, por lo que puede requerir más tiempo al inicio.
- ❌ **Funciones avanzadas:** el uso de **audio o video en Linux** puede requerir una instalación adicional.

### 📊 Resumen comparativo

| Característica | Flet | Tkinter |
|----------------|:----:|:-------:|
| Escritorio | ✅ | ✅ |
| Web | ✅ | ❌ |
| Móvil | ✅ | ❌ |
| Apariencia moderna | ✅ | ➖ |
| Sin HTML/CSS/JS | ✅ | ✅ |
| Ligero para apps pequeñas | ➖ | ✅ |
| Compatible con Python < 3.10 | ❌ | ✅ |
| Curva de aprendizaje inicial | Mayor | Menor |

---

## 8. Ejemplo mínimo: contador interactivo

La aplicación muestra un **contador que inicia en cero**. Cada vez que el usuario presiona el botón **"Incrementar"**, el número aumenta en uno y la interfaz se actualiza automáticamente.

### 💻 Código

```python
import flet as ft


def main(page: ft.Page):
    page.title = "Contador interactivo"

    contador = 0
    texto = ft.Text(value=str(contador), size=40)

    def incrementar(e):
        nonlocal contador
        contador += 1
        texto.value = str(contador)
        page.update()

    boton = ft.ElevatedButton(text="Incrementar", on_click=incrementar)

    page.add(texto, boton)


ft.app(target=main)
```

### 🔍 Explicación del funcionamiento

#### 🪟 Ventana principal: `main(page: ft.Page)`

La ventana principal se crea mediante esta función. El parámetro **`page`** representa la pantalla principal y permite:

- Agregar componentes.
- Establecer el título.
- Organizar la interfaz.

#### 🧩 Componentes gráficos

Se crean con clases de Flet:

| Componente | Uso en el ejemplo |
|------------|-------------------|
| `ft.Text` | Muestra el **valor del contador**. |
| `ft.ElevatedButton` | Crea el **botón** que el usuario puede presionar. |

#### 🖱️ Evento implementado: `on_click`

Se activa cuando el usuario hace clic en el botón **"Incrementar"**.

#### ⚡ Función que responde al evento: `incrementar(e)`

Esta función:

1. **Aumenta** en uno el valor de la variable `contador`.
2. **Actualiza** el texto que aparece en pantalla.

#### 🔄 Actualización de la interfaz: `page.update()`

Después de modificar el valor, se llama a este método para que el usuario **vea el nuevo número**.

---

## ✨ Resumen final

| Tema | Idea clave |
|------|-----------|
| **Qué es** | Framework de Python para interfaces gráficas |
| **Plataformas** | Escritorio, web y móvil |
| **Requisito** | Python 3.10+ |
| **Instalación** | `pip install flet[all]` |
| **Elementos básicos** | Controles (`Page`, `Text`, `Button`, `Row`, `Column`...) |
| **Eventos** | `on_click` + `page.update()` |
| **Frente a Tkinter** | Más moderno y multiplataforma, pero más pesado |
